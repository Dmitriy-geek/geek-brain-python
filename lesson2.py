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
print("Задача №2 введите текст- ")
inputN = input()
inputN = inputN.split()
n = 0
if (len(inputN) // 2) != 0:
    n = len(inputN) - 1
for i in range(0, (len(inputN) - 1), 2):
    c = inputN[i]
    m = inputN[i + 1]
    inputN[i] = m
    inputN[i + 1] = c
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

string_all= input("Введите текст")
string = string_all.split(' ')
for i in range(0, (len(string))):
    count = str(i+1)
    word = list(string[i])
    if len(word)>=11:
        n = string[i]
        string[i]= n[1:11]
    print(count, '.' , string[i])


# Rеализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если
# в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.
print("Задача №5 сортировка списка")
my_list = [3, 5, 8, 90]
new_int = int(input("Введите число"))
count = 1
my_list.append(new_int)
while count > 0:
    count = 0 # счетчик исправлений для выхода из цикла
    n = len(my_list)
    for i in range(0, n):
        c = i + 1 # переменная для обхода ошибки out of range index
        if c == n:
            c = i
        print(i, c)
        if my_list[i] < my_list[c]:
            n = my_list.pop(i)
            my_list.append(n)
            count = 1
            break
print(my_list)

