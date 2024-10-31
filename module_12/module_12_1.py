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
    def test_walk(self):
        runner = Runner('Default1')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)   
         
    def test_run(self):
        runner = Runner('Default2')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100) 
        
    def test_challenge(self):
        runner3 = Runner('Default')
        runner4 = Runner('Default')
        for i in range(10):
            runner3.walk()
            runner4.run()
        self.assertNotEqual(runner3.distance, runner4.distance)  
          
if __name__ == "__main__":
    unittest.main()

        