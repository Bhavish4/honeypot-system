from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["honeypot"]

ssh_logs = db["ssh_logs"]
ssh_commands = db["ssh_commands"]
web_logs = db["web_logs"]