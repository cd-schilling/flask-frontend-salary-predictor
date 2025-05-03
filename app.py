from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Flask frontend is running on Azure!"