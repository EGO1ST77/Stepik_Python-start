# Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами,
# равными 10 в соответствии с образцом:
#
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
# Примечание. Для вывода треугольника используйте цикл for.

def draw_triangle():
    for i in range(10):
        print((1 + i) * '*')
    print()

draw_triangle()