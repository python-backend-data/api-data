"""
Servidor
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/v1/data")
def get_data():
    return jsonify({"data" : "data"})


def main():
    return 123
