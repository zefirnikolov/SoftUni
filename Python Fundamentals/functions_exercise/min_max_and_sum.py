def min_max_sum(digits):
    digit_list = digits.split()
    int_digit_list = [int(x) for x in digit_list]  # Make the strings in the split list into digits.
    min_digit = min(int_digit_list)
    max_digit = max(int_digit_list)
    sum_digits = sum(int_digit_list)
    return f"The minimum number is {min_digit}\nThe maximum number is {max_digit}\nThe sum number is: {sum_digits}"


numbers = input()
print(min_max_sum(numbers))
