import time

class Video:   

    def __init__ (self, title: str, duration: int, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode      
    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title                
class User:
    def __init__ (self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __str__(self):
        return self.nickname
    def __repr__(self):
        return self.nickname
    def __eq__(self, other):
        if isinstance(other, User):
            return other.nickname == self.nickname
    def get_info(self):
        return self.nickname, self.password
        
class UrTube:
    users = []
    videos = []
    
    def __init__ (self):
        self.current_user = None
        
    def register (self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print (f"Пользователь {nickname} уже существует")        
    
    def log_in(self, login, password):
        # global current_user, users
        for user in self.users:
            if (login, hash(password)) == user.get_info():
                self.current_user = user
                return
            else:
                print ('Пользователь не найден')

                
    def log_out(self):
        self.current_user = None
        print('Вы вышли из аккаунта')
        
    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
        # print(videos)

    def get_videos(self, search):
        titles = []
        # print(self.videos)
        for video in self.videos:
            if search.lower() in video.title.lower():
                titles.append(video)
            # print(titles)
        return titles 
                                
    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт чтобы смотреть видео")
            return None

        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, покиньте пожалуйста страницу")
                    return None
                while video.time_now < video.duration:
                    video.time_now += 1
                    print(video.time_now)
                    time.sleep(1)
                video.time_now = 0
                print("Конец видео")

    
ur = UrTube()
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