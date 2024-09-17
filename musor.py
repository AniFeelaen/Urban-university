class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        return f'{self.name}, {self.weight}, {self.category}\n'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read().splitlines()

    def add(self, *products):
        existing_products = self.get_products()
        for product in products:
            if product.name in map(lambda p: p.name, existing_products):
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                with open(self.__file_name, 'a+') as file:
                    file.write(f'{product}\n')
                    
