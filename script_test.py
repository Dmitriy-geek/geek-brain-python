#первая задача
from sys import argv

try:
    script_name, first_param, second_param, third_param = argv
    n = int(first_param)*int(second_param)+int(third_param)
    print(n)
except ValueError:
    print("Введите числа 24 1000 1300, где первое часы работы, второе ставка, а третье премия")
    
# вторая задача
print("lan" , "вторая задача")
import random

my_list = []

for i in range(13):
    my_list.append(random.randint(0, 500))

new_list = []
n = my_list[0]
for el in my_list:
    if n < el:
        new_list.append(el)
    n = el
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")

# третья задача
print("третья задача")

print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')


# четвертая задача
my_list = [2, 5, 2, 7, 23, 23, 44, 44, 3, 2, 10, 7, 4, 11]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)


# пятая задача

from functools import reduce

def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el

my_list = [el for el in range(100, 1001, 2)]
print(my_list)
print(reduce(my_func, my_list))

# шестая задача
from itertools import count
from itertools import cycle

for el in count(int(input("Введите цифру от 0 до 10"))):
    if el > 15:
        break
    else:
        с =0
        for el in cycle(("нельзя казнить помиловать").split()):
            if с > 6:
                break
            print(el)
            с += 1
        print(el)


# седьмая задача

from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
for i in gen:
    if x < 4:
        print(i)
        x += 1
    else:
        break
