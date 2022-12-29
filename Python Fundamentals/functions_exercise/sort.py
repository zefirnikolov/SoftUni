def sorter_in_list(digits):
    digit_list = digits.split()
    int_digit_list = [int(x) for x in digit_list]  # Make the strings in the split list into digits.
    sorted_digit_list = sorted(int_digit_list)
    return sorted_digit_list


numbers_input = input()
print(sorter_in_list(numbers_input))

# numbers_input = input()
# numbers_list = numbers_input.split()
# int_numbers_list = [int(x) for x in numbers_list]
# sorted_numbers_list = sorted(int_numbers_list)
# print(sorted_numbers_list)
