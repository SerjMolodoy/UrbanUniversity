import unittest
from tests_12_3_1 import RunnerTest
from tests_12_3 import TournamentTest

# Создаем TestSuite
suite = unittest.TestSuite()

# Используем TestLoader для добавления тестов из классов
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(RunnerTest))
suite.addTest(loader.loadTestsFromTestCase(TournamentTest))

# Создаем TextTestRunner с verbosity=2
runner = unittest.TextTestRunner(verbosity=2)

# Запускаем тесты
runner.run(suite)