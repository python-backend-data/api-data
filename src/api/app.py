"""
Servidor
"""
from flask import Flask, jsonify
from typing import Optional
from api.repo import Repo
from api.config import Config

app = Flask(__name__)
config = Config()
repo: Optional[Repo] = Repo(config.configuracion["data_path"])

datos = repo.datos  # type: ignore
lista_items = repo.lista_items  # type: ignore


@app.route("/api/v1/data")
def get_data():
    return jsonify({"items": lista_items})


@app.route("/api/v1/data/<string:item>")
def get_data_item(item):

    return jsonify({"item": item, "dato": datos[item]})


def main():
    return 123


if __name__ == "__main__":
    app.run(debug=True, port=4000)
