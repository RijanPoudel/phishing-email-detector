import re
import joblib

model = joblib.load("models/phishing_model.pkl")

SUSPICIOUS_KEYWORDS = [
    "verify",
    "password",
    "login",
    "urgent",
    "bank",
    "click here",
    "account",
    "suspended",
    "confirm"
]

def analyze_email(text):
    urls = re.findall(r'https?://\S+', text)

    keyword_hits = []

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword.lower() in text.lower():
            keyword_hits.append(keyword)

    prediction = model.predict([text])[0]
    probability = model.predict_proba([text])[0][1]

    return {
        "phishing": bool(prediction),
        "confidence": round(probability * 100, 2),
        "url_count": len(urls),
        "keywords_detected": keyword_hits
    }
