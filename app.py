from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_url = "https://salary-api-cdschilling-duanedh7cbdehfecm.centralus-01.azurewebsites.net/predict"

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        education = request.form["education"]
        experience = request.form["experience"]

        response = requests.post(api_url, json={
            "education": education,
            "experience": int(experience)
        })

        if response.status_code == 200:
            prediction = response.json().get("prediction")
        else:
            prediction = "Error getting prediction."

    return render_template("index.html", prediction=prediction)