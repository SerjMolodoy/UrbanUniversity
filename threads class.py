from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int, enemy: int = 100):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = enemy

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        while self.enemy > 0:
            sleep(1)
            days += 1
            self.enemy -= self.power
            print(f'{self.name} сражается {days} день(дня)...,',
                      f'осталось {self.enemy} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
