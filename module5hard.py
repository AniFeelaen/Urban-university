import time

class Video:   

    def __init__ (self, title: str, duration: int, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode                      
class User:
    def __init__ (self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(self.password)
        self.age = age
        
class UrTube:
    
    def __init__ (self, users, videos, current_user):
        self.users = []
        self.videos = []
        self.current_user = None
    
    def log_in(self, login, password):
        # global current_user, users
        for user in self.users:
            if login == user.nickname and hash(password) == user.password:
                self.current_user == user
            else:
                print ('Пользователь не найден')
    
    def register (self, nickname, password, age):
        for user in self.users:
            if nickname not in user.nickname:
                user = User(nickname, password, age)
                self.users.append(user)
                self.log_out()
                self.log_in(user.nickname, user.password)
            else:
                print (f"Пользователь {self.nickname} уже существует")
                break
    
    def log_out(self):
        self.current_user = None
        print('Вы вышли из аккаунта')
        
    def add(self, *Video):
        titles = []
        for video in self.videos:
            if self.title not in Video:
                Video.append(self.title)
            else:
                pass
    def get_videos(self, request):
        result_of_request = []
        for video in self.videos:
            if request.lower in video.title.lower():
                result_of_request.append(video.title)
            return result_of_request                
            
    def watch_video(self, title):
        if self.log_in:
            
            for video in self.videos:
                if video.title == title:
                    print(video.time)
                    print(time.sleep(1))
                else:
                    pass
            pass
        else:
            print("Войдите в аккаунт, чтобы смотреть")
    
ur = UrTube("vasya_pupkin",10, True)
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')