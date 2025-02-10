import unittest
from functools import wraps

from runner import Runner
from runner_and_tournament import Tournament


def skip_if_frozen(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        instance = args[0]
        if instance.is_frozen:
            return unittest.skip("Тесты в этом кейсе заморожены")(func)(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper

class Runner:
    def __init__(self, name, speed=5):  # Добавляем аргумент speed со значением по умолчанию
        self.name = name
        self.distance = 0
        self.speed = speed  # Инициализируем скорость

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
class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for test_name, results in cls.all_results.items():
            formatted_results = {k: str(v) for k, v in results.items()}
            print(f"{test_name}: {formatted_results}")

    @skip_if_frozen
    def test_race_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.all_results['test_race_usain_nick'] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @skip_if_frozen
    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.all_results['test_race_andrey_nick'] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @skip_if_frozen
    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.all_results['test_race_usain_andrey_nick'] = results
        self.assertTrue(results[max(results.keys())] == "Ник")
