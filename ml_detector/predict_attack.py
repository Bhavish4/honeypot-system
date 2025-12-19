import pickle
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))

def predict_attack(payload):
    payload = payload.lower()
    vector = vectorizer.transform([payload])

    prediction = model.predict(vector)[0]
    confidence = np.max(model.predict_proba(vector))

    if confidence < 0.60:
        return "Unknown_Attack", round(confidence, 2)

    return prediction, round(confidence, 2)
