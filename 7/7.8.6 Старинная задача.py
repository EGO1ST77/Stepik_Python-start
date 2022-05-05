'''
Имеется 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги,
если плата за быка – 10 рублей, за корову – 55 рублей, за теленка – 0.5 рубля и надо купить 100 голов скота?

Примечание. Используйте вложенный цикл for.
'''

s = 100
total = 100
for bulls in range(0, 100):
    for cows in range(0, 100):
        for calf in range(0, 100):
            if 10*bulls + 5*cows + 0.5*calf == 100:
               if 100 % (bulls + cows + calf) == 0:
                    if bulls + cows + calf == 100:
                        print('bulls =', bulls, 'cows =', cows, 'calf =', calf)

