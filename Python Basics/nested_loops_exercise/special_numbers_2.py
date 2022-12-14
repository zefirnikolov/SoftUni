number = int(input())
for current_number in range(1111, 9999 + 1):
    is_number_special = True
    current_number_to_string = str(current_number)
    for current_digit in current_number_to_string:
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            is_number_special = False
            break
    if is_number_special:
        print(current_number, end=" ")
