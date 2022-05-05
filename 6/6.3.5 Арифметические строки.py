'''Вводятся 3 строки в случайном порядке.'''
'''Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.'''

a, b, c = len(input()), len(input()), len(input())

mmin = min(a, b, c)
mmax = max(a, b, c)
mmidle = ((a + b + c)/3)

if mmax - mmidle == mmidle - mmin:
    print('YES')
else:
    print('NO')