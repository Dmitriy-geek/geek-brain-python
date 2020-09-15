# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# text = input("Введите текст слова, цифры и символы") .. так и не нашел легкий способ,
# преобразования текста "555" , "ееее" в 555 , "ееее"... остальное долго через сравнения и проверки
print("Задача №1")
text = [555, False, 34.00, "доброе утро", "45"]
n = len(text)
for i in range(len(text)):
    print(type(text[i]), text[i])
# второй способ
# print(list(map(type, text)))

# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем
# месте. Для заполнения списка элементов необходимо использовать функцию input().
print("Задача №2 введите слово- ")
inputN = list(input("напишите слово"))
for i in range(1, len(inputN), 2):
    c = inputN[i-1]
    m = inputN[i]
    inputN[i-1] = m
    inputN[i] = c
print(inputN)


#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и через dict.
print("Задача №3 введите месяц от 1 до 12- ")
input_month = int(input())
n = 0
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
n = winter
for i in range(0, (len(n))):
    if n[i] == input_month:
        print("Это зима")
        break
n = spring
for i in range(0, (len(n))):
    if n[i] == input_month:
        print("Это весна")
n = summer
for i in range(0, (len(n))):
    if n[i] == input_month:
        print("Это лето")
n = autumn
for i in range(0, (len(n))):
    if n[i] == input_month:
        print("Это осень")

# "Задача №3 через словарь, введите месяц от 1 до 12- "
print("Задача №3 через словарь, введите месяц от 1 до 12- ")
input_month_d = int(input())

dictW = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
for el in dictW:
    n = dictW.get(el)
    c = el
    for i in range(0, (len(n))):
        if n[i] == input_month_d:
            print(c)


# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово
# с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые
# 10 букв в слове.
print("Задача №4 строки в слова и сократить вывод до 10-ти букв ")

my_string= input("Введите строку с пробелами между словами").split()

for i, word in enumerate(my_string, 1):
    print(f' {i} . {word[:10]}')


# Rеализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если
# в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.
print("Задача №5 ")
my_list = [3, 5, 3, 8, 90]
count = 1
while count > 0: # сортировка списка
    count = 0 # счетчик исправлений для выхода из цикла
    n = len(my_list)
    for i in range(0, n):
        c = i + 1 # переменная для обхода ошибки out of range index
        if c == n:
            c = i
        if my_list[i] < my_list[c]:
            n = my_list.pop(i)
            my_list.append(n)
            count = 1
            break
new_int = int(input("Введите число"))
pos = len(my_list) + my_list.count(new_int)
print(pos)
my_list.insert(pos, new_int)
print(my_list)

# задача 6
print('Задача №6')
goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': '', }
analis = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Для выхода из программы нажмите Q').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        property = input(f'Введите значение "{f}":')
        features[f] = int(property) if (f == 'цена' or f == 'количество') else property
        analis[f].append(features[f])
    goods.append((num, features))
    print(f'\n Текущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analis.items():
        print(f'{key:>30}:{value}')
    print("*" * 30)