from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the model
model = joblib.load("model.pkl")

# Example input keys: adjust to match your actual input fields
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    try:
        # Extract values from JSON and convert to model input
        education = data.get("education")
        experience = data.get("experience")

        # Manually map categorical values to numbers (example)
        education_map = {"Bachelors": 0, "Masters": 1, "PhD": 2}
        education_val = education_map.get(education, -1)

        # Format input for model
        model_input = np.array([[education_val, int(experience)]])
        prediction = model.predict(model_input)[0]

        return jsonify({"prediction": round(prediction, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)