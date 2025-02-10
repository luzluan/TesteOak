from flask import Flask, Blueprint, request, jsonify
from classproduct import Product
import json


app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, Zina!"

@app.route("/cadastro", methods=['POST', 'GET'])
def cadastro():
    return "Ronaldo"

if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)
