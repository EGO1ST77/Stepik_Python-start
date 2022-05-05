'''x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 - x2) == (y1 - y2) and (x1 + x2) == (y1 + y2) or (x1 - x2) * (y1 - y2) == 2 or (x1 - x2) * (y1 - y2) == -2:
    print('YES')
else:
    print('NO')'''

a, b, c, d = int(input()), int(input()), int(input()), int(input())
x = a - b
y = c - d
x = (x**2)**0.5
y = (y**2)**0.5

if (a - c)**2 == (b - d)**2 or (x == 1 and y == 2) or (x == 2 and y == 1):
    print("YES")
else:
    print("NO")