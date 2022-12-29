from math import floor

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


def distance_from_0(_x1, _y1, _x2, _y2):
    return (_x2 - _x1) ** 2 + (_y2 - _y1) ** 2


x1y1 = distance_from_0(x1, y1, 0, 0)
x2y2 = distance_from_0(x2, y2, 0, 0)
x3y3 = distance_from_0(x3, y3, 0, 0)
x4y4 = distance_from_0(x4, y4, 0, 0)

first_line = x1y1 + x2y2
second_line = x3y3 + x4y4

if first_line >= second_line:
    if x1y1 <= x2y2:
        print(f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})')
    else:
        print(f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})')
if first_line < second_line:
    if x3y3 <= x4y4:
        print(f'({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})')
    else:
        print(f'({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})')
