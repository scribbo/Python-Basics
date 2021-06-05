# Task_1

import time


class TrafficLight:
    __color = 'Red'

    def running(self):
        while True:
            print(self.__color)
            time.sleep(7)
            self.__color = 'Yellow'
            print(self.__color)
            time.sleep(2)
            self.__color = 'Green'
            print(self.__color)
            time.sleep(5)
            self.__color = 'Red'


tl = TrafficLight()
tl.running()


# Task_2


class Road:
    def __init__(self, length, width):
        self._l = length
        self._w = width

    def my_weight(self):
        sum_w = self._l * self._w * (25/1000) * (5/100)
        print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна длиной {self._l} метров и шириной {self._w} метров составляет {sum_w} тонн.')


road1 = Road(100, 500)
road1.my_weight()

# Task_3

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.n = name
        self.s = surname
        self.p = position
        self._income = {'wage': wage, 'bonus': bonus}
        self.w = wage
        self.b = bonus


class Position(Worker):
    def get_full_name(self):
        print(f'{self.n} {self.s}')

    def get_total_income(self):
        tot = self._income.get('wage') + self._income.get('bonus')
        print(tot)


person = Position('Иван', 'Иванович', 'стажер', 20000, 5000)
person.get_full_name()
person.get_total_income()

# Task 4


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.s = speed
        self.c = color
        self.n = name
        self.p = bool(is_police)

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.d = direction
        print(f'Машина повернула на{self.d}')

    def show_speed(self):
        print(f'Скорость автомобиля равна {self.s} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.s > 60:
            print('Вы превысили скорость')
        print(f'Скорость автомобиля равна {self.s} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.s > 40:
            print('Вы превысили скорость')
        print(f'Скорость автомобиля равна {self.s} км/ч')


class PoliceCar(Car):
    pass


mazda = TownCar(65, 'red', 'ZZ')
mazda.go()
mazda.stop()
mazda.turn('право')
mazda.show_speed()
print(mazda.p)

volga = WorkCar(35, 'blue', '07')
volga.go()
volga.stop()
volga.turn('лево')
volga.show_speed()
print(volga.c)
print(volga.p)

ferrari = SportCar(120, 'yellow', 'F1')
ferrari.go()
ferrari.stop()
ferrari.turn('право')
ferrari.show_speed()
print(ferrari.c)
print(ferrari.s)
print(ferrari.p)

ford = PoliceCar(60, 'green', 'focus', True)
ford.go()
ford.stop()
ford.turn('право')
ford.show_speed()
print(ford.c)
print(ford.s)
print(ford.p)

# Task 5


class Stationery:
    def __init__(self, title):
        self.t = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Толщина линии равна 0.5 мм')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш остро заточен')


class Handle(Stationery):
    def draw(self):
        print('Маркер засох')


item_1 = Pen('parker')
item_1.draw()

item_2 = Pencil('bic')
item_2.draw()

item_3 = Handle('attache')
item_3.draw()










