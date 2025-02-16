from classproduct import Product
import json
import os

def prod_add(prod_addition):
    return prod_addition.strip().lower() in ['sim', 'yes', 's', 'y']

db_temp = "db_temp.json"
if os.path.exists(db_temp) and os.path.getsize(db_temp) > 0:
    with open(db_temp, "r", encoding="utf-8") as db:
        try:
            data = json.load(db)
        except json.JSONDecodeError:
            print("Erro: O arquivo JSON está corrompido. Criando um novo arquivo.")
            data = []
else:
    data = []

products_list = []

prod_id = 0

cond_disponibility = True

while cond_disponibility:

    prod_id = prod_id + 1
    prod_name = input("Digite o nome do produto:\n")
    prod_description = input("Insira a descrição do produto\n")
    prod_value = input("Insira o valor do produto:\n")
    prod_disponibility = input("O produto está disponível? 'sim' ou 'não'\n")

    new_product = Product(prod_id, prod_name, prod_description, prod_value, prod_disponibility)

    product_dict = {
        "id": prod_id,
        "name": prod_name,
        "description": prod_description,
        "value": prod_value,
        "disponibility": prod_disponibility
    }

    products_list.append(new_product)
    data.append(product_dict)

    prod_addition = input("Gostaria de continuar adicionando produtos?\nResponda com 'sim' ou 'não'\n")

    if not prod_add(prod_addition):
        break

with open(db_temp, "w") as db:
    json.dump(data, db, indent=4)

for product in products_list:
    print(vars(product))