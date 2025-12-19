from pymongo import MongoClient
import csv
import os
from predict_attack import predict_attack

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "attack_data.csv")

client = MongoClient("mongodb://localhost:27017/")
db = client["honeypot_db"]
web_logs = db["web_logs"]

with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    for log in web_logs.find():
        payload = str(log.get("payload"))
        attack_type, confidence = predict_attack(payload)

        if confidence > 0.80:  # only high-confidence samples
            writer.writerow([payload, attack_type])

print("[+] Dataset updated from real honeypot logs")
