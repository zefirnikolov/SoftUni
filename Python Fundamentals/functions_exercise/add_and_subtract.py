def sum_number(a, b):
    summed = a + b
    return summed


def subtract(sum, c):
    difference = sum - c
    return difference


def add_and_subtract(a, b, c):
    sum_of_first_and_second = sum_number(a, b)
    result = subtract(sum_of_first_and_second, c)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
