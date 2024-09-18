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
        open(self.__file_name, 'r')
        self.__file_name.close
        return self.__file_name.read
    
    def add(self, *products):
        all_products = self.get_products
        for product in products:
            if products in all_products:
                print(f'Продукт {self.name} уже есть в магазине')
            else:
                open(self.__file_name, 'a')
                self.__file_name.write(f'{self.name}, {self.weight}, {self.category}\n')
                self.__file_name.close
            
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())