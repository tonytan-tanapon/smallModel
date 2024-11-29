from flask import Flask, request, jsonify
import joblib
import os
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load the pre-trained model
model_path = "./model/model.pkl"
model = joblib.load(model_path)

# Predefined labels for predictions
label_map = {0: "Negative", 1: "Positive"}

@app.route("/", methods=["GET"])
def home():
    """
    Root route to check API status.
    """
    return jsonify({"message": "Welcome to the Lightweight ML API!"})

@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict sentiment based on input text.
    Expects JSON with a 'text' field.
    """
    data = request.get_json()
    if "text" not in data:
        return jsonify({"error": "Missing 'text' field in request"}), 400

    text = data["text"]
    features = [text]  # For simplicity, we use raw text as features
    prediction = model.predict(features)[0]
    label = label_map[prediction]

    return jsonify({"text": text, "prediction": label})

if __name__ == "__main__":
    # Use PORT environment variable or default to 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
