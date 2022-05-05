'''
На вход программе подается два натуральных числа a и b (a < b).
Напишите программу, которая находит натуральное число из отрезка [a;b] с максимальной суммой делителей.

Формат входных данных
На вход программе подаются два числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести два числа на одной строке, разделенных пробелом:
число с максимальной суммой делителей и сумму его делителей.

Примечание. Если таких чисел несколько, то выведите наибольшее из них.
'''
a, b = int(input()), int(input())
n = 0
count = 0
max_count = 0
sd = 0
max_sum = 0
for i in range(a, b+1):
    count = 0
    sd = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
            sd += j
        if count >= max_count or sd >= max_sum:
            max_count = count
            max_sum = sd
            n = j
    print(': j =', j,  ': count =', count, ': sd =', sd)
print(n, max_sum)



