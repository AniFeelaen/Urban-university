class House:
    def __init__ (self, name, floors):
        self.name = name
        self.number_of_floors = floors
                 
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1 :
                print("Такого этажа не существует")
                return
        for i  in range(1, new_floor + 1) :  #прибавляем к new_floor 1 чтобы включить последний элемент в проверку
            print(i) #после проверки на существование этажа в доме выводим этажи до нового этажа
            
    def __len__(self):
        return self.number_of_floors
    
    def __str__(self):#выводим в консоль строки объекта
        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")
    
    def __eq__(self, other):#сравниванием количество этажей
        if isinstance(other, House):
            if self.number_of_floors == other.number_of_floors:
                return True
            else :
                return False
    def __it__(self, other):#сравниванием количество этажей
        if isinstance(other, House):
            if self.number_of_floors < other.number_of_floors:
                return True
            else :
                return False  
    def __le__(self, other):#сравниванием количество этажей
        if isinstance(other, House):
            if self.number_of_floors <= other.number_of_floors:
                return True
            else :
                return False       
    def __gt__(self, other):#сравниванием количество этажей
        if isinstance(other, House):
            if self.number_of_floors > other.number_of_floors:
                return True
            else :
                return False     
    def __ge__(self, other):#сравниванием количество этажей
        if isinstance(other, House):
            if self.number_of_floors >= other.number_of_floors:
                return True
            else :
                return False               
    def __ne__(self, other):#сравниванием количество этажей
        if isinstance(other, House):
            if self.number_of_floors != other.number_of_floors:
                return True
            else :
                return False        
        
    def __add__(self, value): #добавляем value к этажам
        if isinstance(value, int):
            self.number_of_floors += value
            return self
    def __radd__(self, value):
        # if isinstance(value, int):
            return self.__add__(value)
    def __iadd__(self, value):
        if isinstance(value, int):
            # self.number_of_floors += value
            # return self        
            return self.__add__(value)
    
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

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

h2 = h2 + 10  # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__