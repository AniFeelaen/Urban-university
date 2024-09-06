class Video:   
    def __init__ (self, title: str, duration: int, time_now, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode                      
class User:
    def __init__ (self, name: str, password: int, age: int):
        self.name = []
        self.password = hash(password)
        self.age = age
class UrTube:
    def __init__ (self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user
    
    def log_in(nickname,password):
        global current_user, users
        if nickname in users and password == hash(password):
            current_user == nickname
            return True
        return False
    def register (self, name, password, age):
        if name not in self.name:
            self.name.append(name)
        else:
            print (f"Пользователь {nickname} уже существует")
        return True
    