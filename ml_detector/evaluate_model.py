import pandas as pd
import pickle
import os
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model & vectorizer
model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))

# Load dataset
data = pd.read_csv(os.path.join(BASE_DIR, "attack_data.csv"))

X = data["payload"]
y_true = data["label"]

# Transform and predict
X_vec = vectorizer.transform(X)
y_pred = model.predict(X_vec)

# Metrics
print("\n🔹 Accuracy:", round(accuracy_score(y_true, y_pred), 3))
print("\n🔹 Classification Report:\n")
print(classification_report(y_true, y_pred))

print("\n🔹 Confusion Matrix:\n")
print(confusion_matrix(y_true, y_pred))
