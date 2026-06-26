from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/usd")
def usd():
    data = requests.get("https://s3.amazonaws.com/dolartoday/data.json").json()
    return jsonify({"usd": data["USD"]["promedio"]})

@app.route("/eur")
def eur():
    data = requests.get("https://s3.amazonaws.com/dolartoday/data.json").json()
    return jsonify({"eur": data["EUR"]["promedio"]})
