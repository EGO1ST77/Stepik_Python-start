'''
На вход программе подается последовательность целых чисел от 1 до 5,
характеризующее оценку ученика, каждое число на отдельной строке.
Концом последовательности является любое отрицательное число, либо число большее 5.
Напишите программу, которая выводит количество пятерок.

Формат входных данных
На вход программе подается последовательность чисел, каждое число на отдельной строке.

Формат выходных данных
Программа должна вывести количество пятерок.
'''

num5 = 0
a = int(input())

while 0 < a < 6:
    if a == 5:
        num5 += 1
    a = int(input())
print(num5)