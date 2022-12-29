def print_header():
    print("Function without parameter")


print_header()

numbers = [1, 3, 4, 5, 6, 10, 12, 13, 50, 22, 14, 33]


def check_numbers(num):
    if num % 2 == 0:
        return True
    else:
        return False


result = list(filter(check_numbers, numbers))
print(result)


def multiply_numbers():
    a = 5
    b = 6
    print(a * b)


multiply_numbers()
check_numbers(8)
int(17)
print(check_numbers(8))
