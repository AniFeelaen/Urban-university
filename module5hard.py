class UrTube:
    def __new__(cls, *args, **kwargs):
        # cls.houses_history.append(args[0])
        return object.__new__(cls)              #обязательное условие возврата значений
    def __init__ (self, name, floors):
        self.name = name
        self.number_of_floors = floors
        
        
class Video:
    def __init__ (self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
           
        
        
        
class User:
    def __init__ (self, name, password, age):
        self.name = name
        self.password = password
        self.age = age