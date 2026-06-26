from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/usd")
def usd():
    data = requests.get("https://open.er-api.com/v6/latest/USD").json()
    return jsonify({"usd": data["rates"]["VES"]})

@app.route("/eur")
def eur():
    data = requests.get("https://open.er-api.com/v6/latest/EUR").json()
    return jsonify({"eur": data["rates"]["VES"]})


