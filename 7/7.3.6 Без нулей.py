'''
Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.

Формат входных данных
На вход программе подаются 10 целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести произведение отличных от нуля чисел.

Примечание. Гарантируется, что хотя бы одно из 10 чисел является ненулевым.
'''

s = 1
for i in range(10):
    n = int(input())
    if n != 0:
        s *= n
print(s)
