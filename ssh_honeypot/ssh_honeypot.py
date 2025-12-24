import socket
import threading
import paramiko
from datetime import datetime
from database.db import ssh_logs, ssh_commands
import logging

logging.getLogger("paramiko").setLevel(logging.CRITICAL)

HOST_KEY = paramiko.RSAKey.generate(2048)

FAKE_FILES = ["bin", "etc", "home", "var", "tmp", "README.txt"]

class SSHServer(paramiko.ServerInterface):
    def __init__(self, client_ip):
        self.client_ip = client_ip

    def check_auth_password(self, username, password):
        ssh_logs.insert_one({
            "ip": self.client_ip,
            "username": username,
            "password": password,
            "time": datetime.utcnow(),
            "type": "Brute Force"
        })
        return paramiko.AUTH_SUCCESSFUL

    def get_allowed_auths(self, username):
        return "password"

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED


def fake_shell(channel, client_ip):
    channel.send(b"Ubuntu 20.04.6 LTS\n")
    channel.send(b"Last login: " + str(datetime.utcnow()).encode() + b"\n\n")

    while True:
        channel.send(b"root@server:~# ")
        command = channel.recv(1024).decode("utf-8").strip()

        if not command:
            continue

        ssh_commands.insert_one({
            "ip": client_ip,
            "command": command,
            "time": datetime.utcnow()
        })

        if command in ("exit", "logout"):
            channel.send(b"logout\n")
            break

        elif command == "whoami":
            channel.send(b"root\n")

        elif command == "pwd":
            channel.send(b"/root\n")

        elif command.startswith("ls"):
            channel.send(("  ".join(FAKE_FILES) + "\n").encode())

        elif command == "uname -a":
            channel.send(
                b"Linux server 5.15.0-84-generic x86_64 GNU/Linux\n"
            )

        else:
            channel.send(
                f"bash: {command}: command not found\n".encode()
            )

    channel.close()


def handle_client(client, addr):
    client.settimeout(10)

    try:
        transport = paramiko.Transport(client)
        transport.add_server_key(HOST_KEY)

        server = SSHServer(addr[0])
        transport.start_server(server=server)

        channel = transport.accept(5)
        if channel:
            fake_shell(channel, addr[0])

    except (paramiko.SSHException, socket.timeout):
        pass
    finally:
        try:
            transport.close()
        except:
            pass
        client.close()


def start_honeypot():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("0.0.0.0", 2222))
    sock.listen(100)

    print("[+] SSH Honeypot running on port 2222")

    while True:
        client, addr = sock.accept()
        threading.Thread(
            target=handle_client,
            args=(client, addr),
            daemon=True
        ).start()


if __name__ == "__main__":
    start_honeypot()
