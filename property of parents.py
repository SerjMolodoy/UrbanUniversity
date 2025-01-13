class Vehicle:
    __COLOR_VARIANTS = ['grey', 'red', 'black', 'white', 'yellow']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_engine_power(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print('\033[34m', self.get_model())
        print(self.get_engine_power())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'\033[37mНельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'Red')

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = '\033[32mVasyok'

vehicle1.print_info()
