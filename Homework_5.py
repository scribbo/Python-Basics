# Task 1

with open("my_file__.txt", 'w', encoding='utf-8') as f:
    while True:
        a = input('Введите данные, для выхода введите пустую строку ')
        if a == '':
            break
        f.writelines(a + '\n')

# Task 2

with open("task_2.txt", 'r', encoding='utf-8') as f:
    i = 0
    for line in f:
        i += 1
        line = line.split()
        l = len(line)
        print(f'В {i} строке {l} слов(а)')
    print(f'Всего в файле {i} строк(и)')

# Task 3

with open("task_3.txt", 'r', encoding='utf-8') as f:
    print('Сотрудники с доходом ниже 20000 руб:')
    mid = []
    for line in f:
        line = line.split()
        mid.append(line[1])
        if float(line[1]) < 20000:
            print(line[0])
    for i in range(len(mid)):
        mid[i] = float(mid[i])
    print(f'Средний доход сотрудников составляет: {sum(mid)/len(mid)}')

# Task 4

a = open("task_4_1.txt", 'w', encoding='utf-8')
with open("task_4.txt", 'r', encoding='utf-8') as f:
    my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for line in f:
        line = line.split()
        line[0] = my_dict.get(line[0])
        print(' '.join(line), file=a)

a.close


# Task 5

with open("task_5.txt", '+w', encoding='utf-8') as f:
    text = input('Введите набор чисел через пробел ')
    my_list = []
    my_list = text.split()
    for i in range(len(my_list)):
        my_list[i] = float(my_list[i])
    f.write(text + '\n')
    f.write(f'Среднее арифметическое = {sum(my_list)/len(my_list)}')

# Task 6

with open("task_6.txt", 'r', encoding='utf-8') as f:
    my_dict = {}
    for line in f:
        num_list = []
        my_list = line.split()
        for i in range(len(my_list)):
            if my_list[i].isnumeric():
                num_list.append(int(my_list[i]))
            my_sum = sum(num_list)
        d = {my_list[0]: my_sum}
        my_dict.update(d)
    print(my_dict)

# Task 7


import json

with open("task_7.txt", 'r', encoding='utf-8') as f:
    my_list = []
    dict_profit = {}
    k = 0
    sum_profit = 0
    for line in f:
        num_list = []
        word_list = line.split()
        for i in range(len(word_list)):
            if word_list[i].isnumeric():
                num_list.append(float(word_list[i]))
        profit = num_list[0] - num_list[1]
        dict_profit.update({word_list[0]: profit})
        if profit >= 0:
            sum_profit += profit
            k += 1
    my_list = [dict_profit, {'average_profit': (sum_profit / k)}]
    print(my_list)

with open("task_7_1.json", 'w', encoding='utf-8') as j_write:
    json.dump(my_list, j_write)













