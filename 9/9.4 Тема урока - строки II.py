# Метод count() - Метод count(<sub>, <start>, <end>) считает количество
# непересекающихся вхождений подстроки <sub> в исходную строку s.
s = 'soo moo too'
print(s.count('oo'))
print(s.count('oo', 0, 8))

# Метод startswith() - Метод startswith(<suffix>, <start>, <end>) определяет
# начинается ли исходная строка s подстрокой <suffix>. Если исходная строка
# начинается с подстроки <suffix>,метод возвращает значение True, а если нет, то  False.
s = 'foobar'
print(s.startswith('foo'))
print(s.startswith('bar'))

# Метод endswith() - Метод endswith(<suffix>, <start>, <end>) определяет оканчивается ли
# исходная строка s подстрокой <suffix>. Метод возвращает значение True если исходная строка
# оканчивается на подстроку <suffix> и False в противном случае.
s = 'foobar'
print(s.endswith('foo'))
print(s.endswith('bar'))

# Методы find(), rfind() - Метод find(<sub>, <start>, <end>) находит индекс первого вхождения
# подстроки <sub> в исходной строке s. Если строка s не содержит подстроки <sub>, то метод
# возвращает значение -1. Мы можем использовать данный метод наравне с оператором in для проверки:
# содержит ли заданная строка некоторую подстроку или нет.
s = 'foo bar foo baz foo qux'
print(s.find('foo'))
print(s.find('bar'))
print(s.find('qu'))
print(s.find('python'))

# Методы index(), rindex() - Метод index(<sub>, <start>, <end>) идентичен методу find(<sub>, <start>, <end>),
# за тем исключением, что он вызывает ошибку  ValueError: substring not found во время выполнения программы,
# если подстрока <sub> не найдена.
#
# Метод rindex(<sub>, <start>, <end>) идентичен методу index(<sub>, <start>, <end>), за тем исключением,
# что он ищет первое вхождение подстроки <sub> начиная с конца строки s.
#
# Методы find() и rfind() являются более безопасными чем index() и rindex(), так как не приводят к
# возникновению ошибки во время выполнения программы.


# Метод strip() - Метод strip() возвращает копию строки s у которой удалены все пробелы стоящие в начале и конце строки.
s = '     foo bar foo baz foo qux     '
print(s.strip())

# Метод lstrip() - Метод lstrip() возвращает копию строки s у которой удалены все пробелы стоящие в начале строки.
s = '     foo bar foo baz foo qux     '
print(s.lstrip())

# Метод rstrip() - Метод rstrip() возвращает копию строки s у которой удалены все пробелы стоящие в конце строки.
s = '     foo bar foo baz foo qux     '
print(s.rstrip())

# Метод replace() - Метод replace(<old>, <new>) возвращает копию s со всеми
# вхождениями подстроки <old>, замененными на <new>.
s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'string'))
print(s.replace('foo', 'string', 2))
