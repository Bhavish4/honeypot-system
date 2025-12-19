import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("attack_data.csv", quotechar='"')

X = data["payload"]
y = data["label"]

vectorizer = TfidfVectorizer(
    ngram_range=(1,2),
    stop_words="english"
)

X_vec = vectorizer.fit_transform(X)

model = LogisticRegression(
    max_iter=2000,
    class_weight="balanced"
)

model.fit(X_vec, y)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("[+] Realistic ML Attack Detection Model Trained")
