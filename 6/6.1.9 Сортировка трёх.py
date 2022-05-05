a, b, c = int(input()), int(input()), int(input())

xmin = min(a, b, c)
xmax = max(a, b, c)
xsum = a + b + c

print(xmax)
print(xsum - xmax - xmin)
print(xmin)