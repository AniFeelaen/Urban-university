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
        self.start()

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
            for table in tables:
                if table.guest is  None :
                    table.guest = guest 
                    guest.start                 
                    print(f'{guest.name} сел(-a) за стол номер {table.number}')
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')                
                       
    def discuss_guests(self):
        while not self.queue.empty():
            for guest in guests:
                for table in tables:
                    if guest.is_alive and table.guest is not None :
                        print(f'{guest.name} покушал и ушел')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None


                    if table.guest is None:
                        new_guest = self.queue.get()
                        table.guest = new_guest
                        print(f'{new_guest.name} вышел из очереди и сел за стол номер {table.number}')
                        # new_guest.join()
                    

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