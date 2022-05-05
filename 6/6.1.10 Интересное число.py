x = int(input())

a = (x // 100) % 10
b = (x // 10) % 10
c = x % 10

xmin = min(a, b, c)
xmax = max(a, b, c)
xsred = (a + b + c) - xmax - xmin

if (xmax - xmin) == xsred - xmax - xmin:    # можно записать : if (a + b + c) = 2 * max(a, b, c):
    print('Число интересное')
else:
    print('Число неинтересное')