# 🛡️ Intelligent Honeypot System with ML-Based Attack Detection

A **live, production-style cybersecurity project** that deploys deceptive network services to attract real attackers, analyze their behavior using **machine learning**, store events in **MongoDB**, and visualize threats on a **SOC-style dashboard**.

---

## 📌 Project Overview

Traditional security systems focus on blocking attacks but provide limited insight into attacker behavior.  
This project implements an **intelligent honeypot system** that intentionally exposes fake vulnerable services to capture real cyber attacks, classify them using machine learning, and present actionable insights through an interactive dashboard.

The system is designed to run **live on a public VPS**, making it suitable for **real-world threat intelligence** and **academic research**.

---

## 🎯 Key Features

- 🔐 **SSH Honeypot** for brute-force and command-based attacks  
- 🌐 **Web Honeypot** with fake admin panel (SQLi, XSS, malware capture)  
- 🧠 **ML-based attack classification** using TF-IDF + Logistic Regression  
- 📊 **Real-time MongoDB-backed security dashboard**  
- 📈 **Confidence-based threat scoring (SOC-style)**  
- 🔄 **Automatic retraining from real honeypot logs**  
- 🚀 **Live deployment on public VPS**

---

## 🧱 System Architecture

```plaintext
Internet (Attackers)
↓
Honeypot Services
├── SSH (Port 2222)
└── Web Admin Panel
↓
Machine Learning Classifier
↓
MongoDB
↓
Security Dashboard (Flask)
```

---

## 🛠️ Technology Stack

| Component         | Technology       |
|-------------------|------------------|
| **Language**      | Python 3         |
| **Web Framework** | Flask            |
| **SSH Emulation** | Paramiko         |
| **Database**      | MongoDB          |
| **Machine Learning** | Scikit-learn  |
| **NLP**           | TF-IDF Vectorizer |
| **Visualization** | Chart.js         |
| **OS**            | Linux (Ubuntu VPS) |

---

## 📁 Project Structure

```plaintext
honeypot-system/
│
├── ssh_honeypot/
│   └── ssh_honeypot.py
│
├── web_honeypot/
│   ├── app.py
│   └── templates/
│       └── login.html
│
├── ml_detector/
│   ├── train_model.py
│   ├── predict_attack.py
│   ├── evaluate_model.py
│   ├── update_dataset_from_logs.py
│   └── attack_data.csv
│
├── dashboard/
│   ├── dashboard.py
│   └── templates/
│       └── index.html
│
├── database/
│   └── db.py
│
├── requirements.txt
└── README.md
```

---

## 🧠 How Machine Learning Works

### 🔹 Training Phase
- Attack payloads are labeled (SQLi, XSS, Brute Force, Malware, etc.)
- Text is converted to numerical features using **TF-IDF**
- **Logistic Regression** learns attack patterns
- Trained model is saved as `model.pkl`

### 🔹 Prediction Phase
- Incoming attack payload → vectorized
- ML predicts **attack type + confidence score**
- Low-confidence predictions are flagged as `Unknown_Attack`

### 🔹 Continuous Learning
- High-confidence real attacks are added to dataset
- Model retrains automatically from live honeypot logs

---

## 📊 Dashboard Features

- **Attack type distribution** (Bar Chart)
- **Average ML confidence per attack** (Line Chart)
- **Real-time data** from MongoDB
- **SOC-style dark UI**

---

## 🚀 Live Deployment Guide

### 1️⃣ Setup VPS (Ubuntu)

Use:
- AWS / DigitalOcean / Oracle Cloud  

**Minimum Requirements**
- 1 GB RAM  
- Public IP

---

### 2️⃣ Install Dependencies

```bash
sudo apt update
sudo apt install python3-pip mongodb -y
pip install flask pymongo scikit-learn paramiko
```

### 3️⃣ Start MongoDB

```bash
sudo systemctl start mongodb
sudo systemctl enable mongodb
```

### ▶️ Running the System

#### 🔐 SSH Honeypot

```bash
python ssh_honeypot/ssh_honeypot.py
```

Connect using:

```bash
ssh root@SERVER_IP -p 2222
```

#### 🌐 Web Honeypot

```bash
sudo python web_honeypot/app.py
```

Access:

```plaintext
http://SERVER_IP/admin
```

#### 📊 Dashboard

```bash
python dashboard/dashboard.py
```

Open:

```plaintext
http://SERVER_IP:5000
```

#### 📈 Model Evaluation

Run:

```bash
python ml_detector/evaluate_model.py
```

**Metrics**
- Accuracy
- Precision
- Recall
- Confusion Matrix

#### 🔄 Auto-Retraining (Live Learning)

```bash
python ml_detector/update_dataset_from_logs.py
python ml_detector/train_model.py
```

(Optional) Schedule with cron for continuous learning.

---

## 🛡️ Security & Safety

- Honeypot runs in isolated environment
- No real credentials stored
- Outbound traffic blocked
- No counter-attacks performed

---

## 🎓 Academic Relevance

- Ideal final-year project (Cybersecurity / CS / IT)
- Covers networking, ML, databases, and security
- Live deployment with real attack data
- Strong viva + resume impact

---

## 🏆 Resume Highlight

Built a live intelligent honeypot system capturing real cyber attacks, classified using machine learning, and visualized via a SOC-style dashboard.

---

## 📚 References

- Lance Spitzner – Honeypots: Tracking Hackers
- OWASP Web Security Testing Guide
- NIST Cybersecurity Framework
- Scikit-learn Documentation

---

## 📌 Disclaimer

This project is intended for **educational and research purposes only**.  
Do not deploy without proper network isolation and legal permissions.

---

## ⭐ Support

If you like this project:

- ⭐ Star the repository
- 🍴 Fork and enhance it

Happy Hacking (Ethically)! 🛡️