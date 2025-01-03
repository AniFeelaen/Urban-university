import logging
import unittest


logging.basicConfig(
    level=logging.INFO,
    filemode='w',
    filename='runner_tests.log',
    encoding='UTF-8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)



class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')
    def run(self):
        self.distance += self.speed * 2
    def walk(self):
        self.distance += self.speed
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# third = Runner('Арсен', 10)

# t = Tournament(101, first, second)
# print(t.start())

class RunnerTest(unittest.TestCase):
    is_frozen = False  
    
    @unittest.skipIf(is_frozen, "заморожен") #декоратор заморозки(спипиф принимает булево значение если да то скип)
    def test_walk(self):
        try:
            runner = Runner('Default1', speed = -1) #передаем отрицательную скорость
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)   #дистанция шагуна равна ли 50
            logging.info('"test_walk" выполнен успешно', exc_info = True)
        except:
            logging.warning("Неправильная скорость у runner", exc_info = True) #пишем exc_info чтобы логировать
            # raise e
    
    @unittest.skipIf(is_frozen, "заморожен")       
    def test_run(self):
        try:           
            runner = Runner(123) # передаем число а не строку
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)  #дистанция бегуна равна ли 100
            logging.info('"test_run" выполнен успешно', exc_info = True)
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info = True) #пишем exc_info чтобы логировать
            # raise exc
    
if __name__ == "__main__":
    unittest.main()

# if __name__ == "__main__":
#     runner = unittest.TextTestRunner(verbosity=2)
#     suite = unittest.TestSuite()
#     suite.addTests([
#         RunnerTest('test_walk'),
#         RunnerTest('test_run'),
#         RunnerTest('test_challenge'),
#         # TournamentTest('test_usain_and_nik'),
#         # TournamentTest('test_andrey_and_nik'),
#         # TournamentTest('test_all_three_runners')
#     ])
#     runner.run(suite)