a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j+1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)
