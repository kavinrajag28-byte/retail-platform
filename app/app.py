from flask import Flask, jsonify
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "4.2.0")

@app.route("/")
def home():
    return jsonify({
        "application": "Retail Platform",
        "version": VERSION,
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "version": VERSION
    }), 200

@app.route("/payment")
def payment():
    return jsonify({
        "payment": "successful",
        "version": VERSION
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
