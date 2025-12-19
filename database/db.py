from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["honeypot_db"]

ssh_logs = db["ssh_logs"]
web_logs = db["web_logs"]
