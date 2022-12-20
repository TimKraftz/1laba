import sys
from math import sqrt


def isNum(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


arr = []
while True:
    a = input('введите число: ')
    if a == "":
        break

    if not isNum(a):
        print('Вы ввели не число')
        sys.exit()

    else:
        arr.append(a)


if len(arr) <= 2:
    print('Вы ввели меньше 3 значений')
    sys.exit()


result = [float(arg) for arg in arr]
result.sort()

x = result[-1]
y = result[-2]
z = result[-3]


def func(x, y, z):
    p = (x + y + z) / 2
    s = sqrt((p * (p - x) * (p - y) * (p - z)))
    print(s)

if x > 0 and y > 0 and z > 0:
    if x + y > z and x + z > y and z + y > x:
        func(x, y, z)
    else:
        print('Такого треугольника нет')
else:
    print('Такого треугольника нет')