'''Часы

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)
'''

'''
for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j)
'''

for i in range(8):
    for j in range(i+1):
        print('*', end='')
    print()  

'''
for i in range(1, 4):
    for j in range(3, 5):
        print(i , j, end=' ')
'''
'''
counter = 0
for i in range(99, 102):
    temp = i
    while temp > 0:
        counter += 1
        temp //= 10
print(counter)
'''