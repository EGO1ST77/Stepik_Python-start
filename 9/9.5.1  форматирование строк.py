'''
Дополните приведенный код, используя форматирование строк с помощью метода format, так чтобы он вывел текст:

«In 2010, someone paid 10k Bitcoin for two pizzas.» (без кавычек).
'''

year = 2010
how = '10K'
money = 'Bitcoin'
s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, how, money)
print(s)