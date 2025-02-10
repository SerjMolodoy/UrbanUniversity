class Runner:
    def __init__(self, name, speed):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if speed < 0:
            raise ValueError("Speed cannot be negative")
        self.name = name
        self.speed = speed

    def walk(self):
        return f"{self.name} is walking at {self.speed} km/h"

    def run(self):
        return f"{self.name} is running at {self.speed} km/h"
