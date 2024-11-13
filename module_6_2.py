class Vehicle:
    __COLOR_VARIANTS = ['синий', 'красный', 'зеленый','черный', 'белый']
    def __init__(self,  owner,  model, engine_power,  color):
        self.owner = owner
        self.__model = model
        self. __engine_power = engine_power
        self.__color = color
    def get_model(self):
        return f'модуль:{self.__model}'

    def get_engine_power(self):
        return f'модуль:{self.__engine_power}'

    def get_color(self):
        return f'модуль:{self.__color}'
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет {new_color}')

    def print_info(self):
        print(f'Владелец {self.owner}')
        print(self.get_model(),self.get_engine_power(),self.get_color())

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

#Текущие цвета __COLOR_VARIANTS = ['синий', 'красный', 'зеленый','черный', 'белый']
vehicle1 = Sedan('Федор', 'Toyota Mark II', 'синий', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('серый')
vehicle1.set_color('черный')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
