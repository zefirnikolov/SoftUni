num_1 = int(input())
num_2 = int(input())

for current_number in range(num_1, num_2 + 1):
    even_digit_sum = 0
    odd_digit_sum = 0
    current_number_as_string = str(current_number)

    for index_its_variable, digit_its_variable in enumerate(current_number_as_string):
        # index = index of the string(letter), digit = the exact value of the index,
        # num1 = 100000; num2 = 100050 in this case - index starts with 0
        # digit starts with 1. - from current num1.

        if index_its_variable % 2 == 0:
            odd_digit_sum += int(digit_its_variable) # For the computer the number starts from 0 which is even,
            # for humans starts in 1 = odd
        else:
            even_digit_sum += int(digit_its_variable)

    if even_digit_sum == odd_digit_sum:
        print(current_number, end=" ")
