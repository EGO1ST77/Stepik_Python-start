'''numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(numbers)):
    print(numbers[i], end='')

for num in numbers:
    print(num, end=' ')

print(*numbers)'''

numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
s = 0
for i in numbers:
    s += i**2
print(s)