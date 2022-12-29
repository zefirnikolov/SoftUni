def multiplication_sign(number_one, number_two, number_three):
    numbers_list = [number_one, number_two, number_three]
    is_there_zero = False
    negative_counter = 0
    for element in numbers_list:
        if element == 0:
            is_there_zero = True
        elif element < 0:
            negative_counter += 1
    if is_there_zero:
        return 'zero'
    elif negative_counter % 2 == 1:
        return 'negative'
    else:
        return 'positive'


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(multiplication_sign(first_number, second_number, third_number))
