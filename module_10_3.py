from threading import Thread, Lock
from time import sleep
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()


    def deposit(self):
        for i in range(100):
            #  with self.lock:
                amount = randint(50, 500)
                self.balance += amount
                sleep(0.001)
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                if self.balance >= 500 and self.lock.locked():
                    sleep(0.001)
                    self.lock.release()
                sleep(0.001)


    def take(self):
        for i in range(100):
            # with self.lock:
                request_amount = randint(50, 500)
                print(f"Запрос на {request_amount}")
                if request_amount <= self.balance:
                    self.balance -= request_amount
                    sleep(0.001)
                    print(f"Снятие: {request_amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    sleep(0.001)
                    self.lock.locked()
                sleep(0.001)

bk = Bank()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')