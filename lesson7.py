# ----------------------------------1----------------------------
'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку
конструктора класса (метод __init__()), который должен принимать
данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
Следующий шаг — реализовать перегрузку метода __str__() для
вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации
операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять
поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки
второй матрицы и т.д.
'''


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return "\n".join(map(str, self.lists))

    def __add__(self, other):
        c = []
        n = len(self.lists) if len(self.lists) > len(other.lists) else len(other.lists)
        while len(self.lists)< n:
            self.lists.append([])
        while len(other.lists)< n:
            other.lists.append([])
        for i in range(n):
            c.append([])
            k = len(self.lists[i]) if len(self.lists[i])> len(other.lists[i]) else len(other.lists[i])
            f = abs(len(self.lists[i]) - len(other.lists[i]))
            for j in range(k):
                if k > (k-f):
                    if len(self.lists[i]) < len(other.lists[i]):
                        self.lists[i].append(0)
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return Matrix(c)


a = [[1, 2, 3], [0, 9, 8]]
b = [[5, 6, 11], [3, 7, 5]]
d = [[7, 9, 4, 5], [3, 7, 5, 9],[0,0,0,0]]
matrix_a = Matrix(a)
matrix_b = Matrix(b)
matrix_d = Matrix(d)
print(f'Matrix first\n[{matrix_a}\n{"*" * 30}')
print(f'Matrix second\n[{matrix_b}\n{"*" * 30}')
print(f'Matrix third\n[{matrix_d}\n{"*" * 30}')
n = matrix_a + matrix_b
n += matrix_d
print(f'Matrix all\n[{n}\n{"*" * 30}')


# ----------------------------------2----------------------------
'''
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность
(класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в
этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер
(для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
 реализовать абстрактные классы для основных классов проекта, проверить на практике работу
 декоратора @property.
'''
from abc import ABC, abstractmethod

class Textil(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def m1(self):
        pass

    @property
    def weight(self):
        return self._weight

    @weight.setter # используем 1000 остальное на склад -)
    def weight(self, weight):
        self._weight = 1000


class Coat(Textil):
    def __init__(self, long, size):
        self.size = size
        self.weight = long

    def m1(self):
        print('пошито пальто')

    @property
    def coat_size(self):
        return self.size

    def get_sqeare(self):
        print(f'{round((self.size/6.5 + 0.5), 2)} метров будет '
                     f'использовано при пошиве пальто')
        return round((self.size/6.5 + 0.5), 2)

class Jacket(Textil):
    def __init__(self, long, h):
        self.h = h
        self.weight = long

    def m1(self):
        print('пошит жакет')

    @property
    def j_size(self):
        return self.h

    def get_sqeare(self):
        print(f'{round((self.h*2 * + 0.3), 2)} метров будет использовано '
               f'при пошиве жакета')

        return round((self.h*2 * + 0.3), 2)

def all_s(n , m):
    return f'{round((a.get_sqeare()*n + b.get_sqeare()*m), 2)} метров будет использовано для вашего числа ' \
           f'пальто и жакетов'

a = Coat(500 , 8)
b = Jacket(800 , 10)
n,m = map(int, input("Сколько вам надо пальто и жакетов, например 5 и 6 - ").split(" "))

print(f'пошит {a.coat_size} размер пальто')
print(f'пошит {b.j_size} рост жакета')
print(all_s(n , m), "\n")




# ----------------------------------3----------------------------
'''
Реализовать программу работы с органическими клетками, 
состоящими из ячеек. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий 
количеству ячеек клетки (целое число). В классе должны быть 
реализованы методы перегрузки арифметических операторов: 
сложение (__add__()), вычитание (__sub__()), 
умножение (__mul__()), деление (__floordiv__()). 
Данные методы должны применяться только к клеткам и 
выполнять увеличение, уменьшение, умножение и обычное 
(не целочисленное) деление клеток, соответственно. 
В методе деления должно осуществляться округление значения 
до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек 
общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять 
только если разность количества ячеек двух клеток больше нуля, 
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей 
клетки определяется как произведение количества ячеек этих 
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей 
клетки определяется как целочисленное деление количества ячеек 
этих двух клеток.
В классе необходимо реализовать метод make_order(), 
принимающий экземпляр класса и количество ячеек в ряду. 
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., 
где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний 
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество 
ячеек в ряду — 5. 
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество 
ячеек в ряду — 5. Тогда метод make_order() вернет строку: 
*****\n*****\n*****.
'''


class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        # self.result = Cell(self.quantity + other.quantity)
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')


    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))
    # при floordiv все поломалось

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

input("enter")
cells1 = Cell(33)
cells2 = Cell(9)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1.make_order(10))
print(cells1 / cells2)