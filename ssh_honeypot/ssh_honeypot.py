import socket
import threading
import paramiko
from datetime import datetime
from database.db import ssh_logs

HOST_KEY = paramiko.RSAKey.generate(2048)

class SSHServer(paramiko.ServerInterface):
    def __init__(self, client_ip):
        self.client_ip = client_ip

    def check_auth_password(self, username, password):
        ssh_logs.insert_one({
            "ip": self.client_ip,
            "username": username,
            "password": password,
            "time": datetime.now(),
            "type": "Brute Force"
        })
        return paramiko.AUTH_FAILED

def handle_client(client, addr):
    transport = paramiko.Transport(client)
    transport.add_server_key(HOST_KEY)
    server = SSHServer(addr[0])

    try:
        transport.start_server(server=server)
        channel = transport.accept(20)
        if channel:
            channel.send("Access Denied\n")
            channel.close()
    except:
        pass

def start_honeypot():
    sock = socket.socket()
    sock.bind(("0.0.0.0", 2222))
    sock.listen(100)
    print("[+] SSH Honeypot running on port 2222")

    while True:
        client, addr = sock.accept()
        threading.Thread(target=handle_client, args=(client, addr)).start()

if __name__ == "__main__":
    start_honeypot()
