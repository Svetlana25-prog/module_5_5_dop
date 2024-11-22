import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        return hash(password)

    def __repr__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.time_now = 0
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

    def __repr__(self):
        return self.title
class UrTube:

    def __init__(self):
        self.current_user = None
        self.users = []
        self.videos = []

    def log_in(self, nickname, password):
        hash_password = User.hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hash_password:
                self.current_user = user
                break
        if self.current_user == None:
            print('Неверный логин или пароль')

    def register(self, nickname, password, age):
        m = False
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                m = True
                break
        if not m:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if all(v.title != video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word = search_word.lower()
        p = []
        for v in self.videos:
            if search_word in v.title.lower():
                p.append(v.title)
        return p

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        video = None
        for v in self.videos:
            if v.title == title:
                video = v
                break

        if not video:
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        for second in range(video.time_now + 1, video.duration + 1):
            print(second, end=' ')
            time.sleep(0.1)
        print('Конец видео')
        video.time_now = 0



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