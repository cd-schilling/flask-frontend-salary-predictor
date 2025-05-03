from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    return jsonify({"message": "API is working!"})

if __name__ == "__main__":
    app.run(debug=True)