'''
На вход программе подается строка текста в которой буква «h» встречается как минимум два раза.
Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов,
заключенную между первым и последним вхождением буквы «h».

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''
s = input()
h = 'h'
s1 = s.find(h) + 1
s2 = s.rfind(h)
s_c = s[s1:s2]
print(s[:s1],  s_c[::-1], s[s2:], sep='')
