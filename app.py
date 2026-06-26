from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.get("/usd")
def usd():
    data = requests.get("https://tasa-dolar-venezuela.vercel.app/api").json()
    return jsonify({"usd": data["promedio"]})

@app.get("/eur")
def eur():
    data = requests.get("https://tasa-dolar-venezuela.vercel.app/api/euro").json()
    return jsonify({"eur": data["promedio"]})
