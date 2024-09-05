class House:
    houses_history = []  #используется во всех функциях класса хаус
    def __new__(cls, *args, **kwargs):
        # if not cls.houses_history:
        # print(args)
        # print(kwargs)
            cls.houses_history.append(args[0])
            return object.__new__(cls)              #обязательное условие возврата значений
    def __init__ (self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def __del__(self):
        print(f"{self.name} снесен, но он останется в истории") # используем self а не название объекта напрямую а далее через точку пишем имя, name, floors и так далее
                   
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
        if isinstance(value, int):
            return self.__add__(value)
    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self        
        
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)        