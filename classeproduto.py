class Product:
    def __init__(self, name, description, value, disponibility):
        self.name = name
        self.description = description
        self.value = float(value)
        self.disponibility = disponibility


def check_disponibility(prod_disponibility):
    if prod_disponibility.lower() in ['sim','não', 'nao', 'yes', 'no']:
        return True
    else:
        return False
