from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/usd")
def usd():
    data = requests.get("https://api.exchangerate.host/latest?base=USD&symbols=VES").json()
    return jsonify({"usd": data["rates"]["VES"]})

@app.route("/eur")
def eur():
    data = requests.get("https://api.exchangerate.host/latest?base=EUR&symbols=VES").json()
    return jsonify({"eur": data["rates"]["VES"]})

