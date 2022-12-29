def calculator(action, a, b):
    if action == "multiply":
        return a * b
    elif action == "divide":
        return int(a / b)
    elif action == "add":
        return a + b
    elif action == "subtract":
        return a - b


operator = input()
number_1 = int(input())
number_2 = int(input())

print(calculator(operator, number_1, number_2))
