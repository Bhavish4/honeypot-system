from flask import Flask, jsonify, render_template
from pymongo import MongoClient
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates")
)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["honeypot_db"]
web_logs = db["web_logs"]

# Dashboard page
@app.route("/")
def home():
    return render_template("index.html")

# API for charts
@app.route("/stats")
def stats():
    pipeline = [
        {
            "$group": {
                "_id": "$attack_type",
                "count": {"$sum": 1},
                "avg_confidence": {"$avg": "$confidence"}
            }
        },
        {"$sort": {"count": -1}}
    ]
    data = list(web_logs.aggregate(pipeline))
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
