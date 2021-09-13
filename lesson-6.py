#1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
#Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time
class TrafficLight:
    count = 0
    def __init__(self, color):
        self.__color = color
        if TrafficLight.count == 3:
            TrafficLight.count = 0
        TrafficLight.count += 1

    def running(self):
        if self.__color == 'Красный' and TrafficLight.count == 1:
            print(f'Горит цвет {self.__color}')
            time.sleep(7)
        elif self.__color == 'Желтый' and TrafficLight.count == 2:
            print(f'Горит цвет {self.__color}')
            time.sleep(2)
        elif self.__color == 'Зелёный' and TrafficLight.count == 3:
            print(f'Горит цвет {self.__color}')
            time.sleep(7)
        else:
            print(f'Неверный цвет')
            TrafficLight.count = 0

svet = TrafficLight('Красный')
svet.running()
svet2 = TrafficLight('Красный')
svet2.running()
svet3 = TrafficLight('Зелёный')
svet3.running()
svet4 = TrafficLight('Красный')
svet4.running()
svet5 = TrafficLight('Желтый')
svet5.running()
svet6 = TrafficLight('Зелёный')
svet6.running()

#2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
# для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.
#Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        return self._length * self._width * 25 * 5

road = Road(20, 5000)
print(road.mass())

#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:
    my_dict = {"wage": 50000, "bonus": 20000}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income + self.my_dict.get('bonus')

worker = Position('Ivan', 'Ivanov', 'Employee', 50000)
print(worker.name)
print(worker.get_full_name())
print(worker.get_total_income())

#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!!!')
        else:
            print(f'Текущая скорость: {self.speed}')

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!!!')
        else:
            print(f'Текущая скорость: {self.speed}')

class SportCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

towncar1 = TownCar(50, 'Red', 'Toyota')
print(towncar1.speed)
print(towncar1.color)
print(towncar1.name)
towncar1.show_speed()

towncar2 = TownCar(70, 'Blue', 'Toyota')
print(towncar2.speed)
print(towncar2.color)
print(towncar2.name)
towncar2.go()
towncar2.turn('Налево')
towncar2.stop()
towncar2.show_speed()

#5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        print(f'Запускаем отрисовку: {self.title}')

class Pensil(Stationery):

    def draw(self):
        print(f'Начинаем отрисовку: {self.title}')

class Handle(Stationery):

    def draw(self):
        print(f'Стартуем отрисовку: {self.title}')

pen = Pen('Ручка')
pen.draw()
pensil = Pensil('Карандаш')
pensil.draw()
handle = Handle('Маркер')
handle.draw()
