# # Task 1
#
#
# class Date:
#     def __init__(self, date):
#         self.date = date
#
#     @classmethod
#     def num_date(cls, obj):
#         my_date = obj.date.split('-')
#         print(f'число = {int(my_date[0])}, месяц = {int(my_date[1])}, год = {int(my_date[2])}')
#
#
#     @staticmethod
#     def correct_date(obj):
#         my_date = obj.date.split('-')
#         list_31 = [1, 3, 5, 7, 8, 10, 12]
#         d = int(my_date[0])
#         m = int(my_date[1])
#         y = int(my_date[2])
#         if m == 2 and y % 4 == 0 and d > 29:
#             print('В феврале високосного года только 29 дней')
#         elif m == 2 and y % 4 != 0 and d > 28:
#             print('В феврале невисокосного года только 28 дней')
#         elif m in list_31 and 1 <= d <= 31 and y > 0:
#             print('Введенная дата верна')
#         elif m not in list_31 and 1 <= d <= 30 and y > 0:
#             print(f'Введенная дата верна.')
#         else:
#             print('Введенная дата не верна')
#
#
# a = Date('35-03-2021')
# b = Date('01-04-2015')
# Date.num_date(a)
# Date.correct_date(a)
# Date.num_date(b)
# Date.correct_date(b)


# # Task 2
#
# class DelError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# a, b = list(map(int, input('Введите делимое и делитель через пробел ').split()))
#
# try:
#     if b == 0:
#         raise DelError("Делить на ноль нельзя!")
# except (ZeroDivisionError, DelError) as err:
#     print(err)
#     print(1)
# else:
#     print(round(a / b, 2))


##Task 3


# class NumError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# my_list = []
# while True:
#     a = input('Введите элемент списка, для выхода stop ').split()
#     stop_det = 0
#     for el in a:
#         try:
#             for j in range(len(el)):
#                 if ord(el[j]) < 48 or ord(el[j]) > 57:
#                     raise NumError('Необходимо вводить только числа')
#         except NumError as err:
#             print(err)
#             if el.title() == 'Stop':
#                 stop_det = 1
#                 break
#         else:
#             my_list.append(el)
#     if stop_det == 1:
#         break
#
# print(my_list)

# Task 4, 5, 6


from abc import ABC, abstractmethod


class Hardware(ABC):
    def __init__(self, name, port):
        self.name = name
        self.port = port

    @abstractmethod
    def __str__(self):
        pass


class Printer(Hardware):
    def __init__(self, name, port, color):
        super().__init__(name, port)
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, bool):
        if bool in ['True', 'true', 'Yes', 'yes', 'y', 'Y', 'да', 'Да', '+', 'color', 'Color', True]:
            self.__color = True
        else:
            self.__color = False

    def __str__(self):
        if self.__color:
            return 'Color printer ' + str(self.name) + ' on a tcp port ' + str(self.port)
        else:
            return 'Black&White printer ' + str(self.name) + ' on a tcp port ' + str(self.port)


class Monitor(Hardware):
    def __init__(self, name, port, w, h):
        super().__init__(name, port)
        self.resolution = str(w) + 'x' + str(h)

    def __str__(self):
        return 'Monitor ' + str(self.name) + ' on a ' + str(self.port) + ' port ' + self.resolution


class Scanner(Hardware):
    def __init__(self, name, port):
        super().__init__(name, port)

    def __str__(self):
        return 'Scanner ' + str(self.name) + ' on a ' + str(self.port) + ' port'


class Warehouse:
    def __init__(self):
        self.hw_list = []
        self.count = 0

    def get_count(self):
        return self.count

    def add_hardware(self, my_hardware: Hardware, qtty):
        try:
            for i in range(qtty):
                self.hw_list.append(my_hardware)
            self.count += qtty
        except TypeError:
            print('Quantity shall be an integer number')

    def move(self, other, ordnum):
        if len(self.hw_list) >= ordnum:
            other.add_hardware(self.hw_list[ordnum], 1)
            print(f'{self.hw_list[ordnum]} is moved successfully')
            del self.hw_list[ordnum]
            self.count -= 1
        else:
            print('Hardware index is out of range')

    def __str__(self):
        my_string = ''
        for el in self.hw_list:
            my_string += str(el) + '\n'
        my_string = my_string + 'Total amount of hardware on central warehouse: ' + str(self.count)
        return my_string


central_wh = Warehouse()
central_wh.add_hardware(Printer('LSB-20', 'usb', 'Да'), 'two')
central_wh.add_hardware(Monitor('Viewsonic', 'pci-e', 640, 480), 5)
central_wh.add_hardware(Scanner('HP', 'usb'), 3)
IT = Warehouse()
Accounting = Warehouse()

central_wh.move(IT, 4)
central_wh.move(Accounting, 9)

print('IT:')
print(IT)
print('Accounting:')
print(Accounting)
print('Whs:')
print(central_wh)

# # Task 7
#
# class Complex:
#     def __init__(self, re, im):
#         self.re = re
#         self.im = im
#
#     def __add__(self, other):
#         return Complex(self.re + other.re, self.im + other.im)
#
#     def __mul__(self, other):
#         return Complex(self.re * other.re - self.im * other.im, self.re * other.im + other.re * self.im)
#
#     def __str__(self):
#         if self.im > 0:
#             return str(self.re) + '+' + str(self.im) + 'i'
#         elif self.im < 0:
#             return str(self.re) + str(self.im) + 'i'
#         else:
#             return str(self.re)
#
#
# z = Complex(5, 0)
# z1 = Complex(5, 4)
# z2 = Complex(5, -3)
# print(z)
# print(z1)
# print(z2)
# print(z1 + z2)
# print(z1 * z2)
