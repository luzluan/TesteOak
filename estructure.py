from classproduct import Product
import json

def prod_add(prod_addition):
    if prod_addition.lower() in ['sim', 'yes', 's', 'y']:
        return True
    else:
        return False

with open("db_temp.json", "r", encoding="UTF-8") as file:
    prod_list = json.load(file)



prod_list = []

prod_id = 0

cond_disponibility = True

while cond_disponibility:

    prod_id = prod_id + 1
    prod_name = input("Digite o nome do produto:\n")
    prod_description = input("Insira a descrição do produto\n")
    prod_value = input("Insira o valor do produto:\n")
    prod_disponibility = input("O poroduto está disponível? 'sim' ou 'não'\n")

    prod = Product(prod_id, prod_name, prod_description, prod_value, prod_disponibility)
    prod_list.append(prod)

    prod_addition = input("Gostaria de continuar adicionando produtos?\nResponda com 'sim' ou 'não'\n")

    if prod_add(prod_addition):
        pass
    else:
        cond_disponibility = False

with open("db_proxy.json", "r", encoding="UTF=8") as file:
    json.dump(prod_list, file, intend=4)

for i in range(len(prod_list)):
    print(vars(prod_list[i]))

