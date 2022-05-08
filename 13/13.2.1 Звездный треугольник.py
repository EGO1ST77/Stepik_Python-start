# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
#
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его.
#
# Примечание. Гарантируется, что основание треугольника – нечетное число.

from math import ceil


# объявление функции
def draw_triangle(fill, base):
    m = ceil(base / 2)
    for i in range(base):
        if i < m:
            for j in range(i + 1):
                print(fill, end='')
        else:
            for k in range(m - 1):
                print(fill, end='')
            m -= 1
        print()


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
