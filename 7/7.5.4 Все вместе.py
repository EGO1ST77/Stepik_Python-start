'''
Дано натуральное число. Напишите программу, которая вычисляет:

сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.
'''

num = int(input())
a = 0
summ = 0
how_num = 0
multiplied = 1
average = 0
first = 0
sum1_2 = 0
last = num % 10

while num != 0:
    a = num % 10
    summ += a
    how_num += 1
    multiplied *= a
    average = summ / how_num
    first = a
    sum1_2 = first + last
    num //= 10

print(summ)
print(how_num)
print(multiplied)
print(average)
print(first)
print(sum1_2)
