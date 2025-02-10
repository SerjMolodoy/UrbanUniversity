import unittest
from functools import wraps

from runner import Runner


def skip_if_frozen(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        instance = args[0]
        if instance.is_frozen:
            return unittest.skip("Тесты в этом кейсе заморожены")(func)(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)
