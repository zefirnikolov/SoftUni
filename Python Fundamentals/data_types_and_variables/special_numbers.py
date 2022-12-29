number = int(input())

for current_number in range(1, number + 1):
    is_special = False
    current_number_sum = 0
    print(f"{current_number}", end='')

    while current_number != 0:
        current_number_sum += current_number % 10
        current_number = int(current_number / 10)

    if current_number_sum == 5 or current_number_sum == 7 or current_number_sum == 11:
        is_special = True

    print(f" -> {is_special}")
