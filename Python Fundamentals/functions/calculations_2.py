def calculator(action, a, b):
    result = None
    if action == "multiply":
        result = a * b
    elif action == "divide":
        result = int(a / b)
    elif action == "add":
        result = a + b
    elif action == "subtract":
        result = a - b
    return result


operator = input()
number_1 = int(input())
number_2 = int(input())

print(calculator(operator, number_1, number_2))
