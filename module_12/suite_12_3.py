import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('Default1')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)   #дистанция шагуна равна ли 50
         
    def test_run(self):
        runner = Runner('Default2')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)  #дистанция бегуна равна ли 100
        
    def test_challenge(self):
        runner3 = Runner('Default')
        runner4 = Runner('Default')
        for i in range(10):
            runner3.walk()
            runner4.run()
        self.assertNotEqual(runner3.distance, runner4.distance)   #сравниваем 50 не равно 100
          

class TournamentTest(unittest.TestCase):
    
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
            
    def test_usain_and_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        last_runner = max(results.keys())
        self.assertEqual(results[last_runner], 'Ник') #сравниваем результат последнего раннера с самым медленным(ником)
        self.__class__.all_results['Тест Усэйн и Ник'] = results
        
    def test_andrey_and_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        last_runner = max(results.keys())
        self.assertEqual(results[last_runner], 'Ник')
        self.__class__.all_results['Тест Андрей и Ник'] = results
        
    def test_all_three_runners(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        results = tournament.start()
        last_runner = max(results.keys())
        self.assertEqual(results[last_runner], 'Ник')
        self.__class__.all_results['Тест всех трех'] = results
        
if __name__ == "__main__":
    unittest.main()
