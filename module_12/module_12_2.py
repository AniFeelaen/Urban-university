import unittest
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
                    finishers[place] = participant.name #participant.NAME - получаем имя а не объект для сравнения и сравниваем его потом с "Ник"
                    place += 1
                    self.participants.remove(participant)

        return finishers
    
    
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

if __name__ == '__main__':
    unittest.main()