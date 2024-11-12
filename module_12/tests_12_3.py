import unittest
from suite_12_3 import RunnerTest, TournamentTest
import suite_12_3



suite = unittest.TestSuite()
# suite.addTests([
#     RunnerTest('test_walk'),
#     RunnerTest('test_run'),
#     RunnerTest('test_challenge'),
#     TournamentTest('test_usain_and_nik'),
#     TournamentTest('test_andrey_and_nik'),
#     TournamentTest('test_all_three_runners')
#     ])
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(suite_12_3.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(suite_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)