from flask import Flask, Blueprint, request, jsonify
from classeproduto import Product, check_disponibility

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, Zina!"

@app.route("/cadastro", methods=['POST', 'GET'])
def cadastro():
    return jsonify(products)

if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)
