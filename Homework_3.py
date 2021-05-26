# Task 1
def my_del(var_1, var_2):
    return round(var_1 / var_2, 2)

a = float(input('Введите делимое '))
# b = float(input('Введите делитель '))

if b == 0:
    print('Деление на ноль невозможно')
else:
    print(f'Частное двух чисел равно {my_del(a,b)}')

# Task 2
def my_data(name, surname, date, place, email, tel_num):
    print(f'{name} {surname} {date} года рождения, город {place}, {email}, телефон: {tel_num}')
    return

a = input('Введите имя ')
b = input('Введите фамилию ')
c = input('Введите год рождения ')
d = input('Введите город проживания ')
e = input('Введите email ')
f = input('Введите номер телефона ')

my_data(name=a, surname=b, date=c, place=d, email=e, tel_num=f)

# Task 3


def sum_max(var_1, var_2, var_3):

    if var_1 <= var_2 and var_1 <= var_3:
        return var_2 + var_3
    if var_2 >= var_3:
        return var_1 + var_2
    return var_1 + var_3


while True:
    a = input('a = ')
    if a.split()[0].title() == 'Stop':
        break

    a = float(a)
    b = float(input('b = '))
    c = float(input('c = '))
    print(sum_max(a, b, c))
    print('=== для выхода наберите STOP вместо а ===')

# Task 4.1

def my_power(var_1, var_2):
    return round(var_1 ** var_2, 4)


a = float(input('Введите число. a = '))
b = int(input('Введите степень (целое отрицательное число). b = '))
print(my_power(a, b))

# # Task 4.2


a = float(input('Введите число. a = '))
b = int(input('Введите степень (целое отрицательное число). b = '))


def my_power(var_1, var_2):
    c = 1

    if var_2 >= 0:
        return 'Введите отрицательное число в качестве степени '
    for i in range(-1 * var_2):
        c = c/var_1
    return round(c, 4)


print(my_power(a, b))


# Task 5

def my_summ(num_list, current_sum):

    for el in num_list:
        current_sum += int(el)

    return current_sum

sum = 0

print('Введите ряд чисел через пробел')
while True:
    user_input = input()
    elements = user_input.split()
    if elements == [] or elements[0].title() == 'Stop':
        print(f'Итоговая сумма: {sum}')
        break
    sum = my_summ(elements, sum)
    print(f'Промежуточная сумма: {sum}')
    print('Введите ещё числа, либо stop для выхода из программы')

# Task 6

def title_func(word):
    return word.title()


user_input = input('Введите текст ')
elements = user_input.split()
if elements != [] and elements[0].title() != 'Stop':
    for i in range(len(elements)):
        elements[i] = title_func(elements[i])
    my_str = " ".join(elements)
    print(my_str)



