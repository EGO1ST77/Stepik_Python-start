'''
Все вместе 2
Дано натуральное число. Напишите программу, которая вычисляет:

количество цифр 3 в нем;
сколько раз в нем встречается последняя цифра;
количество четных цифр;
сумму его цифр, больших пяти;
произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.
'''

num = int(input())
n3 = 0
last = num % 10
last_count = 0
chet = 0
sum5 = 0
sum7 = 1
sum05 = 0

while num != 0:
    n = num % 10
    if n == 3:
        n3 += 1
    if n == last:
        last_count +=1
    if n % 2 == 0:
        chet += 1
    if n > 5:
        sum5 += n
    if n > 7:
        sum7 *= n
    if n == 0 or n == 5:
        sum05 +=1
    num = num // 10
print(n3)
print(last_count)
print(chet)
print(sum5)
print(sum7)
print(sum05)

'''
n = int(input())

while n // 1000:
    n = n // 10
print(n % 10)
'''
'''
n = int(input())

if 2 < n < 20:
    print(19 * "*")
    for i in range(2, n):
        print("*", 15*' ', '*')
    print(19 * "*")
'''
'''
count = 0
maximum = -100000000
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
'''
'''
n = 8
count = 0
maximum = -1000000
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
'''

'''
n = int(input())
s = 0
while n > 0:
    if n % 2 == 0:
        s += n % 10
    n //= 10
print(s)
'''

