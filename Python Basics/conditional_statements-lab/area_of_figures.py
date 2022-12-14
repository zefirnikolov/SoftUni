from math import pi

figure = input()
area = 0

if figure == "square":
    a = float(input())
    area = a * a
    print(f'{(a * a):.3f}')
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    print(f'{(a * b):.3f}')
elif figure == "circle":
    radius = float(input())
    area = pi * radius ** 2
    print(f'{(pi * radius * radius):.3f}')
elif figure == "triangle":
    a = float(input())
    b = float(input())
    area = a * b / 2
    print(f'{(a * b / 2):.3f}')
