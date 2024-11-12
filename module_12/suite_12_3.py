import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name
    
class RunnerTest(unittest.TestCase):
    is_frozen = False
    
    @unittest.skipIf(is_frozen, "заморожен") #декоратор заморозки(спипиф принимает булево значение если да то скип)
    def test_walk(self):
        runner = Runner('Default1')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)   #дистанция шагуна равна ли 50
    
    @unittest.skipIf(is_frozen, "заморожен")       
    def test_run(self):
        runner = Runner('Default2')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)  #дистанция бегуна равна ли 100
    
    @unittest.skipIf(is_frozen, "заморожен")     
    def test_challenge(self):
        runner3 = Runner('Default')
        runner4 = Runner('Default')
        for i in range(10):
            runner3.walk()
            runner4.run()
        self.assertNotEqual(runner3.distance, runner4.distance)   #сравниваем 50 не равно 100
        
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
                    finishers[place] = participant.name #participant.NAME - получаем имя а не объект для сравнения и сравниваем его потом с "Ник"
                    place += 1
                    self.participants.remove(participant)

        return finishers
 
class TournamentTest(unittest.TestCase):
    is_frozen = True
    # Создаём атрибут класса для хранения результатов всех тестов
    all_results = {}
    
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        
    def setUp(self):
        # Создаем трех участников забега
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)
        
    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")  #выводим место и имя
            
    @unittest.skipIf(is_frozen, "заморожен") #декоратор заморозки(спипиф принимает булево значение если да то скип)       
    def test_usain_and_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        last_runner = max(results.keys())
        self.assertEqual(results[last_runner], 'Ник') #сравниваем результат последнего раннера с самым медленным(ником)
        self.__class__.all_results['Тест Усэйн и Ник'] = results
        
    @unittest.skipIf(is_frozen, "заморожен")     
    def test_andrey_and_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        last_runner = max(results.keys())
        self.assertEqual(results[last_runner], 'Ник')
        self.__class__.all_results['Тест Андрей и Ник'] = results
        
    @unittest.skipIf(is_frozen, "заморожен")    
    def test_all_three_runners(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        results = tournament.start()
        last_runner = max(results.keys())
        self.assertEqual(results[last_runner], 'Ник')
        self.__class__.all_results['Тест всех трех'] = results

# Указываем переменную на созданный объект TestSuite


# if __name__ == "__main__":
    # runner = unittest.TextTestRunner(verbosity=2)
    # suite = unittest.TestSuite()
    # suite.addTests([
    #     RunnerTest('test_walk'),
    #     RunnerTest('test_run'),
    #     RunnerTest('test_challenge'),
    #     TournamentTest('test_usain_and_nik'),
    #     TournamentTest('test_andrey_and_nik'),
    #     TournamentTest('test_all_three_runners')
    # ])
    # runner.run(suite)