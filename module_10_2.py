from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies_left = 100
    
    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        while self.enemies_left > 0:
            
            self.enemies_left -= self.power
            sleep(1)
            print(f'{self.name}сражается {days} дней, (осталось {self.enemies_left} воинов.)')
            days += 1    
        if self.enemies_left == 0 :   
            print(f'{self.name} одержал победу спустя {days} дней(дня)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения