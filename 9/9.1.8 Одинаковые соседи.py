'''
На вход программе подается одна строка. Напишите программу,
которая определяет сколько в ней одинаковых соседних символов.

Формат входных данных
На вход программе подается одна строка.

Формат выходных данных
Программа должна вывести количество одинаковых соседних символов.
'''

s = input()
neighbor = 0

for i in s:
    if str(i) == s:
        neighbor += 1
    s = str(i)
print(neighbor)