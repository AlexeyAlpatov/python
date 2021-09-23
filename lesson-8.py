#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
# 01-01-2021

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_numbers(cls, date):
        numbers = date.split('-')
        return numbers

    @staticmethod
    def valid_numbers(date):
        numbers = date.split('-')
        if int(numbers[2]) in list(range(0, 2022)):
            if int(numbers[0]) in list(range(0, 31)) and int(numbers[1]) in [1, 3, 5, 7, 8, 10, 12]:
                print('Валидация успешна')
            elif int(numbers[0]) in list(range(0, 30)) and int(numbers[1]) in [4, 6, 9, 11]:
                print('Валидация успешна')
            elif int(numbers[0]) in list(range(0, 29)) and int(numbers[1]) in [2]:
                print('Валидация успешна')
            else:
                print('Валидация провалена')
        else:
            print('Валидация провалена')

print(Date.get_numbers('01-01-2021'))
Date.valid_numbers('25-09-1592')

#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class ZeroDevExcept(Exception):
    def __init__(self, text):
        self.text = text

a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
try:
    if b == 0:
        raise ZeroDevExcept('Делить на ноль нельзя')
except ZeroDevExcept as error:
    print(error)
else:
    print(a / b)

#3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
#Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
#Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class NumberException(Exception):
    def __init__(self, element):
        self.element = element

    def __str__(self):
        if self.element.isdigit() == False:
            return 'Введенное значение не является числом'
        else:
            return 'Добавлено'

my_list = []
cycle = True
while cycle == True:
    elem = input('Введите элемент списка (для завершения введите stop): ')
    if elem == 'stop':
        cycle = False
    else:
        error = NumberException(elem)
        print(error)
        if str(error) == 'Добавлено':
            my_list.append(elem)

print(my_list)

#4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
#5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.
#6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
# уроках по ООП.

dict_store = {}
dict_eq = {}

class Store:
    def __init__(self, name):
        self.name = name

    def add_office_eq(self, list_eq):
        dict_store[self.name] = list_eq
        # дописать заполнение словаря склада

class OfficeEq:
    def __init__(self, type, price, model, count, param):
        self.type = type
        self.price = price
        self.model = model
        self.count = count
        self.param = param

    def add_new_eq(self):
        list_eq_attr = [self.type, self.model, self.price, self.count, self.param]
        #дописать заполнение словаря с оборудованием

class Printer(OfficeEq):
    name = 'Принтер'
    def __init__(self, type, price, model, count, printer_param):
        self.type = type
        self.price = price
        self.model = model
        self.count = count
        self.printer_param = printer_param

class Scanner(OfficeEq):
    name = 'Сканнер'
    def __init__(self, type, price, model, count, scanner_param):
        self.type = type
        self.price = price
        self.model = model
        self.count = count
        self.scanner_param = scanner_param

class Xerox(OfficeEq):
    name = 'Ксерокс'
    def __init__(self, type, price, model, count, xerox_param):
        self.type = type
        self.price = price
        self.model = model
        self.count = count
        self.xerox_param = xerox_param

store = Store('Склад Первый')
printer1 = Printer(Printer.name, '15000 р.','HP1000', '10', 'P_P')
scanner1 = Scanner(Scanner.name, '10000 р.','HPS10', '20', 'S_P')
xerox1 = Xerox(Xerox.name, '5000 р.','HPX1', '30', 'X_P')

#7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    # re - вещественная часть комплексного числа
    # im - мнимая часть комплексного числа
    def __init__(self, re, im):
        self.re = int(re)
        self.im = int(im)

    def __str__(self):
        if self.re != 0:
            if self.im > 0:
                out = f'{self.re} + {self.im}i'
            elif self.im < 0:
                out = f'{self.re} - {abs(self.im)}i'
            else:
                out = f'{self.re}'
        else:
            if self.im != 0:
                out = f'{self.im}i'
            else:
                out = 0
        return out

    def __add__(self, other):
        __sum_re = self.re + other.re
        __sum_im = self.im + other.im
        if __sum_re != 0:
            if __sum_im > 0:
                out = f'{__sum_re} + {__sum_im}i'
            elif __sum_im < 0:
                out = f'{__sum_re} - {abs(__sum_im)}i'
            else:
                out = f'{__sum_re}'
        else:
            if __sum_im != 0:
                out = f'{__sum_im}i'
            else:
                out = 0
        return out

    def __mul__(self, other):
        __part_1 = int((self.re * other.re) - (self.im - other.im))
        __part_2 = int((self.im * other.re) + (self.re * other.im))
        if __part_1 != 0:
            if __part_2 > 0:
                out = f'{__part_1} + {__part_2}i'
            elif __part_2 < 0:
                out = f'{__part_1} - {abs(__part_2)}i'
            else:
                out = f'{__part_1}'
        else:
            if __part_2 != 0:
                out = f'{__part_2}i'
            else:
                out = 0
        return out

complex1 = Complex('12', '-7')
complex2 = Complex('-2', '11')
print(complex1)
print(complex2)
print(complex1 + complex2)
print(complex1 * complex2)
