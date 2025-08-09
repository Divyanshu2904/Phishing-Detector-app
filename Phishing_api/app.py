# app.py
from flask import Flask, request, jsonify
import joblib
from feature_extractor import extract_features

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status":"ok"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    url = data.get("url", "")
    if not url:
        return jsonify({"error":"Missing url"}), 400
    try:
        features = extract_features(url)
        pred = model.predict([features])[0]  # 1 or 0
        label = "Phishing" if int(pred) == 1 else "Legitimate"
        return jsonify({"result": label})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
