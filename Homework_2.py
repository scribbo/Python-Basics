# #Task 1
#
# name = 'Snow'
# list = ['asdf', 23, 'a', 5, name, 567]
#
# for el in list:
#     print(type(el))
#
# #Task 2
#
# list = []
# while True:
#     a = input('Введите элемент списка, для выхода stop ')
#     if a.title() == 'Stop':
#         break
#     list.append(a)
# for el in range(len(list) // 2):
#     tmp = list[el]
#     list[el] = list[len(list) - el - 1]
#     list[len(list) - el - 1] = tmp
# print(list)

#Task 3.1

# month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
# i = int(input('Введите порядковый номер месяца '))
# if i == 12 or (i <= 2 and i >=1):
#     print(f'{month[i-1]} относится к зиме')
# elif (i <= 5 and i >=3):
#     print(f'{month[i - 1]} относится к весне')
# elif (i <= 8 and i >=6):
#     print(f'{month[i - 1]} относится к лету')
# elif (i <= 11 and i >=9):
#     print(f'{month[i - 1]} относится к осени')
# elif i <= 0 or i > 12:
#     print('Вводимое число должно находится в диапазоне от 1 до 12')
#
# #Task 3.2
#
# dict = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
# i = int(input('Введите порядковый номер месяца '))
# if i == 12 or (i <= 2 and i >=1):
#     print(f'{dict[i]} относится к зиме')
# elif (i <= 5 and i >=3):
#     print(f'{dict[i]} относится к весне')
# elif (i <= 8 and i >=6):
#     print(f'{dict[i]} относится к лету')
# elif (i <= 11 and i >=9):
#     print(f'{dict[i]} относится к осени')
# elif i <= 0 or i > 12:
#     print('Вводимое число должно находится в диапазоне от 1 до 12')

# #Task 4
#
# s = input('Введите строку из нескольких слов, разделённых пробелами ')
# my_list = s.split()
# for el in my_list:
#     print(f'{my_list.index(el) + 1}. {el[:10]}')

#Task 5

# li = [7, 5, 3, 3, 2]
# a = int(input('Введите число '))
# for i in range(len(li)):
#     if a > li[i]:
#         li.insert(i, a)
#         break
# else:
#     li.append(a)
#
# print(li)

#Task 6 #пока только так получилось
number_1 = int(input('Введите  номер первого товара '))
name_1 = input('Введите название первого товара ')
price_1 = float(input('Введите цену первого товара '))
amount_1 = int(input('Введите количество первого товара '))
unit_1 = input('Введите единицы измерения ')
prod_1 = (number_1, {'название': name_1, 'цена': price_1, 'количество': amount_1, 'eд.': unit_1})
number_2 = int(input('Введите  номер второго товара '))
name_2 = input('Введите название второго товара ')
price_2 = float(input('Введите цену второго товара '))
amount_2 = int(input('Введите количество второго товара '))
unit_2 = input('Введите единицы измерения ')
prod_2 = (number_2, {'название': name_2, 'цена': price_2, 'количество': amount_2, 'eд.': unit_2})
number_3 = int(input('Введите  номер третьего товара '))
name_3 = input('Введите название третьего товара ')
price_3 = float(input('Введите цену третьего товара '))
amount_3 = int(input('Введите количество третьего товара '))
unit_3 = input('Введите единицы измерения ')
prod_3 = (number_3, {'название': name_3, 'цена': price_3, 'количество': amount_3, 'eд.': unit_3})
li = [prod_1, prod_2, prod_3]
print(li)


