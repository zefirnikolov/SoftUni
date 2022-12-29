def factorial_division(first, second):
    factorial_one = 1
    factorial_two = 1
    for i in range(first, 0, -1):
        factorial_one *= i
    for i in range(second, 0, -1):
        factorial_two *= i
    return f"{(factorial_one / factorial_two):.2f}"


number_one = int(input())
number_two = int(input())
print(factorial_division(number_one, number_two))
