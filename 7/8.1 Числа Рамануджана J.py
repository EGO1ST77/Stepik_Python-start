'''
Сриниваса Рамануджан – индийский математик, славившийся своей интуицией в области чисел.
Когда английский математик Годфри Харди навестил его однажды в больнице,
он обмолвился, что номером такси, на котором он приехал, было 1729,
такое скучное и заурядное число. На что Рамануджан ответил: "Нет, нет! Это очень интересное число.
Это наименьшее число, выражаемое как сумма двух кубов двумя разными способами". Другими словами:
1729 = 1^3 + 12^3 = 9^3 + 10^3.

Напишите программу, которая находит аналогичные интересные числа.
В ответе запишите первые 5 чисел в порядке возрастания, включая число 1729.

Примечание. Используйте вложенный цикл.
'''
a = 1729
s = [a]
x = 0
if x != 33:
    for i in range(1, 34):
        for j in range(1, 34):
            for k in range(1, 34):
                for l in range(1, 34):
                    for m in range(1, 34):
                        if i**3 + j**3 == k**3 + l**3:
                            if i != j and i != k and i != l and j != k and j != l and j != m and l != m:
                                if i**3 + j**3 != a:
                                    b = i**3 + j**3
                                    if a != b:
                                        if b not in s:
                                            s.append(b)
                                            a = b
print(s)
