# class Figure:
#     sides_count = 0
#     def init(self, __sides, __color, filled: bool):
#         self.filled = filled
#         self.sides = __sides
#         self.color = __color
        
#     def get_color(red: int, green: int, blue: int):
#         return list(red,green,blue)  
      
#     def __is_valid_color(self,r,g,b):
#         if not isinstance(r, int) or not isinstance(g, int) or not isinstance(b, int):
#             print("Неверно введен цвет")
#         elif not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
#             print("Цвет вводится от 0 до 255")
#         else:
#             True    
#     def set_color(r,g,b):
#         self.__color = (r,g,b)
#     def __len__():
#         return sides_count* side_length
             
        
        
        
# class Circle(Figure):
    
    
    
# class Triangle(Figure):    
    
# class Cube(Figure):    
import math

class Figure:
    def __init__(self, color=(0, 0, 0), *sides):
        self.__color = color
        self.sides_count = 0
        self.filled = False
        
        if len(sides) == self.sides_count or not self._Figure__is_valid_sides(*sides):
            sides = [1 for _ in range(self.sides_count)]
            
        self.set_sides(*sides)
    
    # @property
    def sides(self):
        return self._Figure__sides
    
    def get_color(self):
        return self.__color
    
    def _Figure__is_valid_color(self, r, g, b):
        return all([isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b)])
    
    def set_color(self, r, g, b):
        if self._Figure__is_valid_color(r, g, b):
            self.__color = (r, g, b)
    
    def _Figure__is_valid_sides(self, *new_sides):
        return (
            len(new_sides) == self.sides_count and
            all(isinstance(side, int) and side > 0 for side in new_sides)
        )
    
    def get_sides(self):
        return self._Figure__sides
    
    def set_sides(self, *new_sides):
        if self._Figure__is_valid_sides(*new_sides):
            self._Figure__sides = list(new_sides)
    
    def __len__(self):
        return sum(self._Figure__sides)


class Circle(Figure):
    def __init__(self, color=(0, 0, 0), radius=1):
        super().__init__(color, radius)
        self.sides_count = 1
        self.__radius = radius
    
    # @property
    def radius(self):
        return self.__radius
    
    def get_square(self):
        return math.pi * self.radius ** 2


class Triangle(Figure):
    def __init__(self, color=(0, 0, 0), a=1, b=1, c=1):
        super().__init__(color, a, b, c)
        self.sides_count = 3
    
    def get_square(self):
        a, b, c = self._Figure__sides
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    def __init__(self, color=(0, 0, 0), edge_length=1):
        super().__init__(color, edge_length)
        self.sides_count = 12
        self._Figure__sides = [edge_length for _ in range(self.sides_count)]
    
    def get_volume(self):
        return self._Figure__sides[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())