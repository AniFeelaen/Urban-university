class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        if isinstance(food, Fruit):
            print(f'{self.name} съел {food.name}')
            self.fed = True
            return self.fed
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
            return self.alive


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
        
class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)
class Plant:
    def __init__(self, edible = False, name=''):
        self.edible = edible
        self.name = name
class Flower(Plant):
    edible = False
    def __init__(self, name):
        super().__init__(False, name)
class Fruit(Plant):
    edible = True
    def __init__(self, name):
        super().__init__(False, name)

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print('-----')
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)