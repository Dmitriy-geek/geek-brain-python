print("Hi")
h = 123
print(h)
print(bool(h))
print(str(h))
print(float(h))

time = int(input("Enter your time"))
hrs = int(time / 3600)
if hrs < 10:
    hrs = str(10) + str(hrs)

minut = int(time / 60)
if minut < 10:
    minut = str(10) + str(minut)

sec = time % 60
if sec < 10:
    sec = str(10) + str(sec)
time_cor = str(hrs) + ":" + str(minut) + ":" + str(sec)
print(time_cor)

summN = input("enter your N like 3...")
summN = int(summN) + int(summN * 2) + int(summN * 3)
print(summN)

prob = int(input("enter your N> 0 like 356 and Int"))
n = prob % 10
prob = prob // 10
while prob > 0:
    if prob % 10 > n:
        n = prob % 10
    prob = prob // 10
print(n, " - max number")

debit = int(input("enter your debit"))
credit = int(input("enter your credit"))
if debit < credit:
    print("So bad business")
else:
    print('Not bad, you are lucky')
    rent = int((debit - credit) / debit * 1000) / 10
    print("Your gain", rent, "=%")
employers = int(input("how many employees do you have in the company"))
deb_emp: int = (debit - credit) / employers
print("This is a profit of", deb_emp, "rubles per person")


x = int(input("Enter start km"))
y = int(input("Enter goal km"))
i = 1
while x < y:
    x *= 1.1
    i += 1
    print(str(i) + "-й " + "день: " + str(int(x*10000)/10000) + "км")


