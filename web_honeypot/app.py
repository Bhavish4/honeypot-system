from flask import Flask, request, render_template
from datetime import datetime
from database.db import web_logs
from ml_detector.predict_attack import predict_attack

app = Flask(__name__)

# Root route (looks harmless)
@app.route("/")
def home():
    return "<h3>Welcome</h3><p>Nothing interesting here.</p>"

# Fake admin panel (honeypot)
@app.route("/admin", methods=["GET", "POST"])
def fake_admin():
    if request.method == "POST":
        payload = request.form.to_dict()
        payload_str = str(payload)

        # ML prediction
        attack_type, confidence = predict_attack(payload_str)

        # Severity calculation
        if confidence >= 0.85:
            severity = "HIGH"
        elif confidence >= 0.65:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        # Store detailed log
        web_logs.insert_one({
            "ip": request.remote_addr,
            "user_agent": request.headers.get("User-Agent"),
            "endpoint": request.path,
            "method": request.method,
            "payload": payload,
            "attack_type": attack_type,
            "confidence": confidence,
            "severity": severity,
            "time": datetime.utcnow()
        })

    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
