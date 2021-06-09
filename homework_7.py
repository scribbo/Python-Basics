# # Task 1
#
#
# class Matrix:
#     my_list = []
#
#     def __init__(self, my_list):
#         self.list = my_list
#
#     def __str__(self):
#         print(' ')
#         res = ''
#         for i in range(len(self.list)):
#             res += str(self.list[i]) + '\n'
#         return res
#
#     def __add__(self, other):
#         res = []
#         a = self.list
#         b = other.list
#         for i in range(len(a)):
#             if i >= len(b):
#                 b.append([])
#             res.append([])
#             for j in range(len(a[i])):
#                 if j >= len(b[i]):
#                     b[i].append(0)
#                 res[i].append(a[i][j] + b[i][j])
#         return Matrix(res)
#
#
# matrix1 = Matrix([[1, 5, 9], [1, 4, 5], [4, 8, 9]])
# print(matrix1)
#
# matrix2 = Matrix([[1, 5, 7], [6, 8, 9]])
# print(matrix2)
#
# matrix3 = matrix1 + matrix2
# print(matrix3)

# # Task 2
#
#
# from abc import ABC, abstractmethod
#
#
# class Clothes(ABC):
#
#     def __init__(self, name):
#         self.n = name
#         self.s = None
#
#     @property
#     def name(self):
#         return self.n
#
#     @abstractmethod
#     def get_s(self):
#         pass
#
# class Coat(Clothes):
#     def __init__(self, name, v):
#         super().__init__(name)
#         self.v = v
#
#     @property
#     def v(self):
#         return self.__v
#
#     @v.setter
#     def v(self, v):
#         if v < 30:
#             self.__v = 30
#         elif v > 62:
#             self.__v = 62
#         else:
#             self.__v = v
#
#     def get_s(self):
#         self.s = (self.__v / 6.5) + 0.5
#         return self.s
#
#
# class Suit(Clothes):
#     def __init__(self, name, h):
#         super().__init__(name)
#         self.h = h
#
#     @property
#     def h(self):
#         return self.__h
#
#     @h.setter
#     def h(self, h):
#         if h < 120:
#             self.__h = 120
#         elif h > 220:
#             self.__h = 220
#         else:
#             self.__h = h
#
#     def get_s(self):
#         self.s = (2 * self.__h) + 0.3
#         return self.s
#
#
# class Collection:
#     def __init__(self):
#         self.my_list = []
#         self.s = 0
#
#     def add_clothes(self, my_clothes: Clothes):
#         self.my_list.append(my_clothes)
#         self.s += my_clothes.get_s()
#
#     def __str__(self):
#         my_string = ''
#         for el in self.my_list:
#             my_string += 'Площадь ткани для ' + el.name + ' равна ' + str(round(el.get_s(), 2)) + '\n'
#         my_string = my_string + 'Суммарная площадь ткани для всей коллекции равна ' + str(round(self.s, 2))
#         return my_string
#
#
# m_list = Collection()
# m_list.add_clothes(Coat('green coat', 46))
# m_list.add_clothes(Suit('striped suit', 182))
# # print(m_list.s)
# print(m_list)


# Task 3

class Cell:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return f' n = {self.n}'

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        if self.n > other.n:
            return Cell(self.n - other.n)
        else:
            return 'Разность количества ячеек двух клеток должна быть больше нуля'

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __truediv__(self, other):
        if other.n != 0:
            return Cell(self.n // other.n)
        else:
            return 'Количество ячеек клетки - делителя должна быть больше нуля'

    def make_order(self, number):
        if number > 0:
            k = self.n // number
            ost = self.n % number
            my_str = '*' * number
            last_str = '*' * ost
            for i in range(k):
                print(my_str)
            print(last_str)


one = Cell(15)
two = Cell(4)
print(one + two)
print(one - two)
print(one * two)
print(one / two)
one.make_order(14)

