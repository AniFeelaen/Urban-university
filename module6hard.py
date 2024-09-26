class Figure:
    sides_count = 0
    def init(self, __sides, __color, filled: bool):
        self.filled = filled
        self.sides = __sides
        self.color = __color
        
    def get_color(red: int, green: int, blue: int):
        return list(red,green,blue)  
      
    def __is_valid_color(self,r,g,b):
        if not isinstance(r, int) or not isinstance(g, int) or not isinstance(b, int):
            print("Неверно введен цвет")
        elif not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            print("Цвет вводится от 0 до 255")
        else:
            True    
    def set_color(r,g,b):
        self.__color = (r,g,b)
    def __len__():
        return sides_count* side_length
             
        
        
        
class Circle(Figure):
    
    
    
class Triangle(Figure):    
    
class Cube(Figure):    