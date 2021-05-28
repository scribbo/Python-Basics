# Task 1

from sys import argv

ar1, ar2, ar3 = map(float, argv[1:])
salary = ar1 * ar2 + ar3

print(f'Заработная плата составляет {salary} руб')

# Task 2


n = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [n[i] for i in range(1, len(n)) if n[i] > n[i - 1]]
print(new)

# Task 3


my_list = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(my_list)

# Task 4


n = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = [n[i] for i in range(len(n)) for k in range(len(n)) if i != k and n[i] == n[k]]
my_list = [n[i] for i in range(len(n)) if not n[i] in new]

print(my_list)

# Task 5


from functools import reduce


def my_func(el_1, el_2):
    return el_1 * el_2


my_list = [i for i in range(100, 1001) if i % 2 == 0]

print(my_list)
print(f'Произведение всех четных чисел от 100 до 1000 равно {reduce(my_func, my_list)}')

# Task 6

from itertools import count, cycle


for el in count(3, 1):
    if el > 10:
        break
    else:
        print(el)

list = [12, 44, 4, 10, 78, 123]
c = 0
for el in cycle(list):
    if c < 25:
        print(el)
        c += 1
    else:
        break

# Task 7


def fact(n):
    k = 1
    for i in range(1, n + 1):
        k = k * i
        yield(k)


n = int(input('Введите n для вычисления факториала '))

if n == 0:
    print('1')

for el in fact(n):
    print(el)

