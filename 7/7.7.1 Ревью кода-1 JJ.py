'''
Надо исправить 4 ошибки
'''
count = 0
p = 1 # 1 р начинаем с 1, а не с 0
for i in range(1, 11):  # 2 range(1, 10)
    x = int(input())
    if x >= 0:  # 3 Больше либо равно!!!
        p *= x   # менаем с кода: p = p * x
        count += 1   # было: count = count + 1
if count > 0:
    print(count)    # 4 Вместо х count
    print(p)
else:
    print('NO')