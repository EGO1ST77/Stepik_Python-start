'''counter = 0
for i in range(1, 101):
    if i % 10 == 4:
        counter = counter + 1
print(counter)'''

'''total = 0
for i in range(1, 101):
    total = total + i
print(total)'''

'''total = 0
for i in range(10):
    num = int(input())
    total = total + num
average = total / 10
print(average)'''

'''num = int(input())
flag = True

for i in range(2, num ):
    if num % i == 0:
        flag = False

if num == 1:
    print('Это единица, она не простая и не составная')
elif flag == True:
    print('Число простое')
else:
    print('Число составное')'''

total = 0
for i in range(1, 6):
    total +=i
    print(total, end='')

