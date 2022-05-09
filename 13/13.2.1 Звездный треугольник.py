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
    n = base // 2
    m = base - n
    for i in range(n + 1):
        print(fill * i)
    for j in range(m, 0, -1):
        print(fill * j)

# считываем данные
fill = input('Zenklas : ')
base = int(input('Skaicius : '))

# вызываем функцию
draw_triangle(fill, base)
