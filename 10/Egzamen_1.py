'''

s = 'Python'
for i in range(len(s)):
    if i % 3 != 0:
        print(s[i], end='')

'''
'''
s = input()
print(s.replace('1', 'one'))
'''
s = input()
for i in s:
    if i == '@':
        continue
    else:
        print(i, end='')