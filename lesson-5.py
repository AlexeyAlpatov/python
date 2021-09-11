#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

file = open('my_file_1.txt', 'w', encoding="utf-8")
while True:
    string = input('Дописать в файл: ')
    if string == '':
        break
    else:
        file.writelines(string)
file.close()

#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("my_file_2.txt") as file:
    i = 0
    while True:
        content = file.readline()
        if content != '':
            i += 1
            words = content.split(' ')
            count = len(words)
            print(f'Количество слов в строке {i}: {count}')
        else:
            break
print(f'Количество строк в файле: {i}')

#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
# величины дохода сотрудников.

file = open('my_file_3.txt', 'r')
my_list = []
count_emp = 0
salary_emp = 0
while True:
    content = file.readline()
    if content != '':
        words = content.split(' ')
        salary = int(words[1])
        count_emp += 1
        salary_emp = salary_emp + salary
        if salary < 20000:
            my_list.append(words[0])
    else:
        break
print(my_list)
print(salary_emp/count_emp)
file.close()

#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

file = open('my_file_4.txt', 'r', encoding="utf-8")
while True:
    content = file.readline()
    if content != '':
        content_new = content.replace('One', 'Один')
        content_new = content_new.replace('Two', 'Два')
        content_new = content_new.replace('Three', 'Три')
        content_new = content_new.replace('Four', 'Четыре')
        file_new = open("my_file_4_new.txt", 'a', encoding="utf-8")
        file_new.write(content_new + '\n')
        file_new.close()
    else:
        break
file.close()

#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random
file = open('my_file_5.txt', 'w')
count_number = random.randint(1, 10)
for i in range(count_number):
    file.write(str(random.randint(0, 1000)) + ' ')
file.close()
file = open('my_file_5.txt', 'r')
content = file.readline()
numbers = content.split(' ')
summa = 0
for i in range(len(numbers)-1):
    summa = summa + int(numbers[i])
print(summa)
file.close()

#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
# по нему. Вывести словарь на экран.
#Примеры строк файла:
#Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря:
#{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

file = open('my_file_6.txt', 'r', encoding="utf-8")
my_dict = {}
while True:
    content = file.readline()
    if content != '':
        content = content.replace('(л)', '')
        content = content.replace('(пр)', '')
        content = content.replace('(лаб)', '')
        content = content.replace('\n', '')
        content = content.replace('—', '0')
        content = content.replace(':', '')
        words = content.split(' ')
        summa = int(words[1]) + int(words[2]) + int(words[3])
        my_dict[words[0]] = summa
    else:
        break
print(my_dict)
file.close()

#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#3[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

#Подсказка: использовать менеджеры контекста.

import json
dict_firm_profit = {}
dict_firm_losses = {}
with open("my_file_7.txt") as file:
    while True:
        content = file.readline()
        if content != '':
            my_list = content.split(' ')
            profit = int(my_list[2]) - int(my_list[3])
            if profit > 0:
                dict_firm_profit[my_list[0]] = profit
            else:
                dict_firm_losses[my_list[0]] = profit
        else:
            break
my_list = list(dict_firm_profit.values())
summa = 0
for i in range(len(my_list)):
    summa = summa + int(my_list[i])
average_profit = summa / len(my_list)
dict_average = {"average_profit": average_profit}
list_itog = [dict_firm_profit, dict_average, dict_firm_losses]
with open("my_file_7.json", "w") as file_json:
    json.dump(list_itog, file_json)
