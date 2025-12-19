from flask import Flask, request, render_template
from datetime import datetime
from database.db import web_logs
from classifier.attack_classifier import classify_attack

app = Flask(__name__)

@app.route("/admin", methods=["GET", "POST"])
def fake_admin():
    if request.method == "POST":
        payload = request.form.to_dict()
        attack_type = classify_attack(str(payload))

        web_logs.insert_one({
            "ip": request.remote_addr,
            "payload": payload,
            "attack_type": attack_type,
            "time": datetime.now()
        })

    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
