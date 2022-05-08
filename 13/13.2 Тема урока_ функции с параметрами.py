# Функция с параметром
# Draw_box

def draw_box(heigh, widht):
    for i in range(heigh):
        print(widht * "*")

draw_box(3, 5)
print()
draw_box(3, 15)
print()
draw_box(3, 25)

def print_number(a, b, c):
    d = (a + c) // b
    print(d)

print_number(2, 3, 11)