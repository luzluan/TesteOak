class Product:
    def __init__(self, id, name, description, value, disponibility):
        self.id = id
        self.name = name
        self.description = description
        self.value = float(value)
        self.disponibility = bool(disponibility)