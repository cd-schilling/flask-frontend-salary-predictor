from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your deployed API endpoint
api_url = "https://salary-api-cdschilling-duanedh7cbdehfecm.centralus-01.azurewebsites.net/predict"

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        education = request.form.get("education")
        experience = request.form.get("experience")

        try:
            response = requests.post(api_url, json={
                "education": education,
                "experience": int(experience)
            })
            response.raise_for_status()  # will raise for 4xx/5xx errors
            prediction = response.json().get("prediction")
        except requests.exceptions.RequestException as e:
            prediction = f"Request error: {e}"
        except Exception as e:
            prediction = f"Internal error: {e}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)