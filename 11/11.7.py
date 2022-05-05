numbers = [i for i in range(10)]
print(numbers, '<--NUMBERS')
zeros = [0 for i in range(10)]
print(zeros, '<--ZEROS')
squares = [i**2 for i in range(10)]
print(squares, '<--SQUARES')
cub = [i**3 for i in range(10, 21)]
print(cub, '<--CUBE')
chars = [c for c in 'abcdefg']
print(chars)

lines = [input('Ввод : ') for _ in range(int(input('Сколько строк? : ')))]
print(lines)

# четные числа
x = [i for i in range(21) if i % 2 == 0]
print(x, '<-- четные')

num = [i * j for i in range(1, 5) for j in range(2)]
print(num)