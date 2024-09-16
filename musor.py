class User:
    def __init__(self, nickname, hashed_password, age):
        self.nickname = nickname
        self.hashed_password = hashed_password
        self.age = age

    @property
    def is_logged_in(self):
        return self == self.current_user

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
    
    def watch(self, time_now=0):
        if not self.adult_mode or self.current_user.is_logged_in:
            print("Начало воспроизведения")
            for i in range(time_now, self.duration + 1):
                print(i)
                # Использование функции sleep для создания паузы
                time.sleep(1)
            print("Конец видео")
        else:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, hashed_password):
        found_user = next((user for user in self.users if user.nickname == nickname and user.hashed_password == hashed_password), None)
        if found_user:
            self.current_user = found_user
            print("Успешный вход")
        else:
            print("Неверный логин или пароль")

    def register(self, nickname, hashed_password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, hashed_password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print("Регистрация успешна!")

    def log_out(self):
        self.current_user = None
        print("Выход из аккаунта")

    def add_video(self, *videos):
        titles = set()
        for video in videos:
            if video.title not in titles:
                titles.add(video.title)
                self.videos.append(video)

    def search_videos(self, query):
        result = []
        for video in self.videos:
            if query.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, video_title):
        target_video = next((video for video in self.videos if video.title == video_title), None)
        if target_video:
            target_video.watch()
        else:
            print("Видео не найдено")
            
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