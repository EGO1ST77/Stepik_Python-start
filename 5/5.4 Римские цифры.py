a = int(input())

if 1 <= a <= 12:
    if 1 <= a <=3:
        print(a*'I')
    elif a == 4:
        print('IV')
    elif a == 5:
        print('V')
    elif a == 6:
        print('VI')
    elif a == 7:
        print('VII')
    elif a == 8:
        print('VIII')
    elif a == 9:
        print('IX')
    elif a == 10:
        print('X')
    else:
        print('ошибка')
else:
    print('ошибка')