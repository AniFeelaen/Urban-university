class Vehicle:
    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str, __COLOR_VARIANTS: list[str]):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.__COLOR_VARIANTS = __COLOR_VARIANTS
        
    def get_model(self):
        return f"Модель: {self.__model}"
    
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"
    
    def get_color(self):
        return f"Цвет: {self.__color}"
    
    def print_info(self):
        return print(super().get_model(self),"\n",
                     super().get_horsepower(self),"\n",
                     super().get_color(self),"\n",
                     f" Владелец: {self.owner}")
    
    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else: 
            print(f"Нельзя сменить цвет на {new_color}")
        
class Sedan(Vehicle):
    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str, __COLOR_VARIANTS: list[str], __PASSENGERS_LIMIT: int):
        super().__init__(owner, __model, __engine_power, __color, __COLOR_VARIANTS)
        self.__PASSENGERS_LIMIT = 5


__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()