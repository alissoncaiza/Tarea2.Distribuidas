class Product:
    def create(self):
        pass

class ConcreteProductA(Product):
    def create(self):
        print("Product A created")

def factory_method(type):
    if type == "A":
        return ConcreteProductA()
    raise ValueError("Unknown product")
