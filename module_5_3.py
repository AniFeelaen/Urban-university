class House:
    def __init__ (self, name, floors):
        self.name = name
        self.number_of_floors = floors
        # print(type(self.number_of_floors))
        self.go_to     
       
    def go_to(self, new_floor):
        for i  in range(1, new_floor + 1) :  #прибавляем к new_floor 1 чтобы включить последний элемент в проверку
            if new_floor > self.number_of_floors or new_floor < 1 :
                print("Такого этажа не существует")
                break
            print(i) #после проверки на существование этажа в доме выводим этажи до нового этажа 
    def __len__(self):
        return self.number_of_floors
    
    def __str__(self):#выводим в консоль строки объекта
        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")
    
    def __eq__(self, other):#сравниванием количество этажей
        # if isinstance(other, int):
            if self.number_of_floors == other:
                return True
            else :
                return False
    def __it__(self, other):#сравниванием количество этажей
        # if isinstance(other, int):
            if self.number_of_floors < other:
                return True
            else :
                return False  
    def __le__(self, other):#сравниванием количество этажей
        # if isinstance(other, int):
            if self.number_of_floors <= other:
                return True
            else :
                return False       
    def __gt__(self, other):#сравниванием количество этажей
        # if isinstance(other, int):
            if self.number_of_floors > other:
                return True
            else :
                return False    
    def __ge__(self, other):#сравниванием количество этажей
        # if isinstance(other, int):
            if self.number_of_floors >= other:
                return True
            else :
                return False               
    def __ne__(self, other):#сравниванием количество этажей
        # if isinstance(other, int):
            if self.number_of_floors != other:
                return True
            else :
                return False        
        
    def __add__(self, value): #добавляем value к этажам
        # if isinstance(value, int):
            self.number_of_floors += value
            return self
    def __radd__(self, value):
            return self.__add__
    def __iadd__(self, value):
            return self.__add__
    
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__