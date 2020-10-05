'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать
два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором
@staticmethod, должен проводить валидацию числа, месяца и года (например,
месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''
class Data:
    """Строка формата «день-месяц-год» реализована в @classmethod, на уроке 8 по методам Вы сказали что можно применить и
такой подход к конструктору иначе в скобках был бы скучный (self, day_month_year), а ниже не было бы трех self..."""

    def __init__(self, day, month, year):
        #self.day_month_year = str(day_month_year)
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def extract(cls, day_month_year):
        int_date = []

        for i in day_month_year.split():
            if i != '-': int_date.append(i)
        return cls(int(int_date[0]), int(int_date[1]), int(int_date[2]))

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Все верно'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    @staticmethod
    def get_data(self):
        return f'{self.day} {self.month} {self.year}'

print('*' *30, '1 zadacha','*' *30)
input('Enter')
today = Data.extract('11 - 1 - 2001')
print(Data.get_data(today))
print(Data.valid(5 , 1, 2020))
print(today.valid(11, 13, 2044))
print(today.day)



# ----------------------------------- 2----------------------------------------'''

'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем 
нуля в качестве делителя программа должна корректно обработать эту ситуацию и 
не завершиться с ошибкой.
'''

class DivisionByNull(Exception):
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    def divide_by_null(self):
        try:
            return (self.divider / self.denominator)
        except ZeroDivisionError:
            return (f"Деление на ноль недопустимо")

print('*' *30, '2 zadacha','*' *30)
input('Enter')
div = DivisionByNull(10, 0)
print(div.divide_by_null())

# ----------------------------------- 3 ----------------------------------------
'''
Создайте собственный класс-исключение, который должен проверять содержимое списка 
на отсутствие элементов типа строка и булево. Проверить работу исключения на реальном примере. 
Необходимо запрашивать у пользователя данные и заполнять список. 
Класс-исключение должен контролировать типы данных элементов списка.
'''


class Error:
    def __init__(self):
        self.my_list = []

    def my_input(self):

       while True:
            try:
                val = int(input('Введите целое число и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'

print('*' *30, '3 zadacha','*' *30)
input('Enter')
try_except = Error()
print(try_except.my_input())


# ----------------------------------- 4 ----------------------------------------
'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники. 
'''

# ----------------------------------- 5 ----------------------------------------

'''
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники 
на склад и передачу в определенное подразделение компании. Для хранения данных 
о наименовании и количестве единиц оргтехники, а также других данных, можно использовать 
любую подходящую структуру, например словарь.
'''

# ----------------------------------- 6 ----------------------------------------
'''
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых 
пользователем данных. Например, для указания количества принтеров, отправленных 
на склад, нельзя использовать строковый тип данных. 
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» 
максимум возможностей, изученных на уроках по ООП.
'''

class StoreMashines:

    def __init__(self, type, name, price, quantity, *args):
        self.type = type
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Тип:устройства': self.type, 'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'Тип {self.type} модель {self.name} цена {self.price} количество {self.quantity}'

    @classmethod
    def extract(cls, *type_name_price_quantity):
        unit_t, unit, unit_p, unit_q = type_name_price_quantity
        print(unit_t, unit, unit_p, unit_q)
        return cls(unit_t, unit, unit_p, unit_q)

    # @staticmethod
    def reception(self):
        # print(f'Для выхода - Q, продолжение - Enter')
        # while True:
        try:
            unit_t = input(f'Введите тип устройства ')
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Тип:устройства': unit_t, 'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f' {self.type} '


class Scanner(StoreMashines):
    def to_scan(self):
        return f' {self.type} '


class Copier(StoreMashines):
    def to_copier(self):
        return f'{self.type}'

print('*' *30, '4-6 zadacha','*' *30)
input('Enter')
unit_1 = Printer('принтер','hp', 2000, 5)
unit_2 = Scanner('сканер', 'Canon', 1200, 5)
unit_3 = Copier('копир', 'Samsung' ,1500, 1)
StoreMashines.extract('принтер','hp', 2000, 5)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())


# ----------------------------------- 7 ----------------------------------------
'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», 
реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и 
выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
'''

class ComplexCompute:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - self.b * other.b}+ {(self.a * other.b) + (self.b * other.a) } * i'

    def __str__(self):
        return f' z = {self.a} + {self.b} * i'

print('*' *30, '7 zadacha','*' *30)
input('Enter')
z_1 = ComplexCompute(3, -3)
z_2 = ComplexCompute(4, 2)
print(z_1, '\n', z_2, '\n')
print(z_1 + z_2 , '\n')
print(z_1 * z_2 )
