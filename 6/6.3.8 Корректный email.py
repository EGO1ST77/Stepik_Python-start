'''
Напишите программу проверяющую корректность email адреса.
Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки.
'''

mail = input()

if '@' not in mail or '.' not in mail:
    print('NO')
else:
    print('YES')