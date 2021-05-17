
#Task 1
year = 1999
print(year)
print(type(year))

part = 0.65
print(part)
print(type(part))

surname = "Иванова"
print(surname)
print(type(surname))

name = input("Укажите Ваше имя ")
print(name)
age = input("Укажите ваш возраст ")
print(age)

#Task2
time = int(input("Введите время в секундах "))
hour = time // 3600
minute = (time - 3600 * hour) // 60
sec = time % 60
print(f'{hour}:{minute}:{sec}')


#Task3
number = input("Введите целое положительное число ")
number1 = number * 2
number2 = number * 3
sum = int(number) + int(number1) + int(number2)
print(sum)

#Task 4
number = int(input("Введите целое положительное число "))
max_digit = number % 10
while number != 0:
    number = number // 10
    digit = number % 10
    if digit > max_digit:
        max_digit = digit
    else:
        continue
print(f'Самая большая цифра в вашем числе: {max_digit}')

#Task 5
cash = int(input('Введите сумму вашей выручки '))
cost = int(input('Введите сумму ваших издержек '))
if cash > cost:
    print('Ваша фирма работает с прибылью')
    profit = (cash - cost) / cash
    print(f'Рентабельность составляет {profit}')
    number = int(input('Введите численность сотрудников '))
    employee_profit = profit/number
    print(f'Прибыль в расчете на одного сотрудника составляет  {employee_profit}')
else:
    print('Ваша фирма работает в убыток')

#Task 6

distance = int(input('Введите результат спортсмена в первый день тренировок в км '))
max_distance = int(input('Введите желаемый результат спортсмена в результате тренировок в км '))
i = 1
while distance <= max_distance:
    print(f'В {i} день тренировок спортсмен пробежит {distance} км.')
    distance = round((distance * 1.1), 2)
    i += 1

print(f'На {i}-й день спортсмен достиг результата — не менее {max_distance} км.')