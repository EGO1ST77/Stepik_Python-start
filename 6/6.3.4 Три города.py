'''Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города'''
name1, name2, name3 = input(), input(), input()

a = len(name1)
b = len(name2)
c = len(name3)
mmax = max(a, b, c)
mmin = min(a, b, c)

if mmin == a:
    print(name1)
elif mmin == b:
    print(name2)
elif mmin == c:
    print(name3)

if mmax == a:
    print(name1)
elif mmax == b:
    print(name2)
elif mmax == c:
    print(name3)