def min_func(numbers: list):
    return min(numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
all_numbers = [first_number, second_number, third_number]
min_number = min_func(all_numbers)

print(min_func(all_numbers))
