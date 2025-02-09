from flask import Flask, Blueprint, request, jsonify
from classeproduto import Product, check_disponibility

server = Flask(__name__)

produtos = [
    {
        'id': 1,
        'nome' = 'Coca-Cola',
        'descricao' = 'Refrigerante de cola',
        'preco' = 5.00
        'disponibilidade' = True
    },
]

@server.route("/")
def home():
    return "Olá, Zina!"

@server.route("/cadastro", methods=['POST'])
def cadastro():
    data = request.json
    return data['descricao']

if __name__ == "__main__":
    server.run(debug=True)
