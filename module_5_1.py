class House:
    def __init__ (self, name, floors):
        self.name = name
        self.number_of_floors = floors
        # print(name, floors)
        self.go_to
        
    
    
    def go_to(self, new_floor):
        # self.number_of_floors = new_floor   #ошибка переназначать внутри функции параметр self он должен быть = floors
        for i  in range(1, new_floor + 1) :  #прибавляем к new_floor 1 чтобы включить последний элемент в проверку
            if new_floor > self.number_of_floors or new_floor < 1 :
                print("Такого этажа не существует")
                break
            print(i) #после проверки на существование этажа в доме выводим этажи до нового этажа
        
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)        
