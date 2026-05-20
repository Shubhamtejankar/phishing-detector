from flask import Flask, render_template, request, jsonify
import joblib
from feature_extraction import extract_features
import requests

app = Flask(__name__)

model = joblib.load("model/model.pkl")

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Real-time API
@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    url = data.get("url")

    try:
        # Check if site is reachable
        response = requests.get(url, timeout=3)
        status = "Online ✅"
    except:
        status = "Offline ❌"

    # ML Prediction
    features = extract_features(url)
    prediction = model.predict([features])[0]

    if prediction == 1:
        result = "⚠️ Phishing Detected"
    else:
        result = "✅ Safe Website"

    # Extra checks
    security = []
    if "https" in url:
        security.append("🔒 HTTPS Secure")
    else:
        security.append("⚠️ No HTTPS")

    if "login" in url or "verify" in url:
        security.append("⚠️ Suspicious Keywords")

    return jsonify({
        "result": result,
        "status": status,
        "checks": security
    })

if __name__ == "__main__":
    app.run(debug=True)