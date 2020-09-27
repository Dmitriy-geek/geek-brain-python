# задача №1----------------------------------------------------------------------------
import colorama
from colorama import Fore, Back, Style
colorama.init()
import time

class TrafficLight:
    __color = ['Красный','Красно-желтый','Зеленый','Желтый']

    def running(self):
        i = 0
        while i < 4:


            if i == 0:
                print(Fore.RED + f'{TrafficLight.__color[i]}')
                time.sleep(7)
            elif i == 1:
                print(Fore.RED , Back.YELLOW + f'{TrafficLight.__color[i]}')
                time.sleep(2)
            elif i == 2:
                print(Fore.GREEN , Back.RESET + f'{TrafficLight.__color[i]}')
                time.sleep(7)
            elif i == 3:
                print(Fore.YELLOW + f'{TrafficLight.__color[i]}')
                time.sleep(2)
                # i=0
                # continue          это бесконечный цикл. но нам он не нужен тут
            print(Style.RESET_ALL)
            i += 1

Light = TrafficLight()
Light.running()

# задача 2 ------------------------------------------------------------------------------------------
class Road:
    def __init__(self):
        Road._leight = 1000
        Road._width = 20

    def mas_asf (self, brutto, height):
        self.brutto = brutto
        self.height = height
        all_mass = Road._leight * Road._width * brutto * height
        print(f'Масса асфальта для длинны в 1 км и ширины 20м  -   {all_mass} кг или {all_mass/1000} тонн')

all_m = Road()
a = input("Введите толщину асфальта в сантиметрах и его вес в килограммах через пробел ").split(" ")
brutto, height = map(int, a)
print(brutto, height)
all_m.mas_asf(brutto, height)

# задача 3 ------------------------------------------------------------------------------------------

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())

    def get_position(self): # вариант решиения
        print(self.get_full_name())
        print(self.get_total_income())

input('press enter')
a = Position('Peter', 'Moskow', 'Worker', 1000, 500)
print(a.get_full_name())
print(a.get_total_income())
# print(a.get_position()) # вариант решения
b = Position('Serg', 'Prosecka', 'Player', 5000, 10000)
print(b.get_full_name())
print(b.get_total_income())

# задача 4 ------------------------------------------------------------------------------------------
class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        self.speed = self.speed + 40 # при каждом го скорость растет на 40
        return print(f'{self.name} is moved')

    def stop(self):
        self.speed = 0
        return print(f'{self.name} is stopped')

    def turn_right(self):
        return print(f'{self.name} is turned right')

    def turn_left(self):
        return print(f'{self.name} is turned left')

    def show_speed(self):
        return print(f'Current speed {self.name} is {self.speed}')


class TownCar(Car):

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed >= 40:
            return print(f'Speed of {self.name} is higher than allow for town car')
        else:
            return print(f'Speed of {self.name} is normal for town car')

class SportCar(Car):

    def go(self):
        self.speed = self.speed + 80 # при каждом го для спорткара скорость растет на 80
        return print(f'{self.name} is moved')

class WorkCar(Car):

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return print(f'Speed of {self.name} is higher than allow for work car')


class PoliceCar(Car):

    def police(self):
        if self.is_police:
            return print(f'{self.name} is from police department')
        else:
            return print(f'{self.name} is not from police department')

input('press enter')
bmw = SportCar(0, 'Red', 'BMW', False)
pegeot = TownCar(0, 'White', 'Pegeot', False)
kia = WorkCar(0, 'Rose', 'Kia', True)
ford = PoliceCar(0, 'Blue',  'Ford', True)
bmw.turn_left()
ford.police()
print(f'Is {kia.name}  a police car? {kia.is_police}')
pegeot.go()
bmw.go()
print(f'bmw speed is {bmw.speed}')
print(f'pegeot speed is {pegeot.speed}')
bmw.stop()
print(f'bmw speed is {bmw.speed}')
print(f'pegeot speed is {pegeot.speed}')
print(f'ford color is {ford.color}')
pegeot.go()
pegeot.show_speed()


# задача 5 ------------------------------------------------------------------------------------------

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):

    def draw(self):
        print(f"Зарисовка ручкой {self.title} начата")


class Pencil(Stationery):

    def draw(self):
        print(f"Зарисовка карандашом {self.title} начата")

class Handle(Stationery):

    def draw(self):
        print(f"Зарисовка маркером {self.title} начата")

input('press enter')
pen = Pen('Parker')
pencil = Pencil('Звезда')
handle = Handle('MultiMarker')
pen.draw()
pencil.draw()
handle.draw()