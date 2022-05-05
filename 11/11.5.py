ip = '192.168.1.24'
numbers = ip.split('.')    # указываем явно разделитель
print(numbers)

words = ['Python', 'is', 'the', 'most', 'powerful', 'language']
s = '_'.join(words)
print(s)

s = 'BEEGEEK'
chars = list(s)
s = '**'.join(chars)
print(s)

s = 'BEEGEEK'
print('**'.join(s))