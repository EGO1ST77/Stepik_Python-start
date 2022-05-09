# Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр


def suma_integer(integer):
    suma = 0
    while integer != 0:
        suma += integer % 10
        integer = integer // 10
    print("Summa = ", suma)


int_input = int(input("Ввести число, чем больше, тем лучше : "))

suma_integer(int_input)

