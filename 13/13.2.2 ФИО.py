# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
#
# name – имя человека;
# surname – фамилия человека;
# patronymic – отчество человека;
# а затем выводит на печать ФИО человека.
#
# Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.

def print_fio(name, surname, fathername):
    print(surname[0].upper(), name[0].upper(), fathername[0].upper(), sep='')

name = input("Имя : ")
surname = input("Фамилия : ")
fathername = input("Отчество : ")

print_fio(name, surname, fathername)