'''
Исправить код - 5 ошибок
'''

mx = -10**6 - 1
s = 0
for i in range(5):  # 1
    x = int(input())
    if x < 0:
        s += x  # 2
    if 0 > x > mx:  # 3
        mx = x
if s == 0:  # 4
    print('NO')  # 5
else:
    print(s)
    print(mx)
