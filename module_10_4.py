import random
from threading import Thread
from queue import Queue
from time import sleep

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def run(self):
        # Ждем случайным образом от 3 до 10 секунд
        time_to_wait = random.randint(3, 10)
        print(f'{self.name} ждёт...')
        sleep(time_to_wait)
        print(f'{self.name} уходит')

class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)
        self.queue = Queue()
    
    def guest_arrival(self, *guests):
        for guest in guests:
            if self.tables is None in self.tables :
                self.guest.start
                print(f'{guest.name} сел за стол номер {self.table.number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
    
    def discuss_guests(self):
        while not self.queue.empty() or  self.tables is not None:
            if self.tables is not None and not Guest.is_alive:
                print(f'{self.guest.name} покушал и ушел')
            else:
                print(f'Стол номер {Table.number} свободен')
                self.table.guest = None
            
            if not self.queue.empty():
                new_guest = self.queue.get()
                new_guest.start()
                print(f'{new_guest.name} вышел из очереди и сел за стол номер {new_guest.number}')
                

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()