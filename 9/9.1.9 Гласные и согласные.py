'''
На вход программе подается одна строка с буквами русского языка.
Напишите программу, которая определяет количество гласных и согласных букв.

Формат входных данных
На вход программе подается одна строка.

Формат выходных данных
Программа должна вывести количество гласных и согласных букв.

Примечание. В русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е) и
21 согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).
'''

s = input()
gls = 0
sgls = 0

for i in s:
    if str(i.lower()) in 'аеёиоуыэюя':
        gls += 1
    elif str(i.lower()) in 'бвгджзйклмнпрстфхцчшщ':
        sgls += 1
print('Количество гласных букв равно', gls)
print('Количество согласных букв равно', sgls)