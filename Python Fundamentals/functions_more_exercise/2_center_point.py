import math


def distance_find(x_first, y_first, x_second, y_seconds):
    return math.sqrt(math.pow(x_second - x_first, 2.0) + math.pow(y_seconds - y_first, 2.0))


x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))

distance_one = distance_find(x1, y1, 0, 0)
distance_two = distance_find(x2, y2, 0, 0)

if distance_one <= distance_two:
    print(f"({x1}, {y1})")
else:
    print(f"({x2}, {y2})")