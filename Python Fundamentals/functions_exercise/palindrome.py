def palindrome_int_checker(digit):
    int_digits_list = [int(x) for x in str(digit)]
    is_palindrome = False
    if len(int_digits_list) % 2 == 0:
        first_sliced_list = int_digits_list[:len(int_digits_list) // 2:]
        second_sliced_list = int_digits_list[len(int_digits_list) // 2:len(int_digits_list):]
        reversed_second_sliced_list = second_sliced_list[::-1]

        if reversed_second_sliced_list == first_sliced_list:
            is_palindrome = True
    else:
        first_sliced_list = int_digits_list[:len(int_digits_list) // 2:]
        second_sliced_list = int_digits_list[len(int_digits_list) // 2 + 1:len(int_digits_list):]
        reversed_second_sliced_list = second_sliced_list[::-1]

        if reversed_second_sliced_list == first_sliced_list:
            is_palindrome = True
    return is_palindrome


numbers_input = input()
numbers_list = numbers_input.split(", ")
for number in numbers_list:
    print(palindrome_int_checker(number))


# numbers_input = input()
# numbers_l = numbers_input.split(", ")
# for number in numbers_l:
#     number_list = [int(x) for x in str(number)]
#     is_palindrome = False
#     if len(number_list) % 2 == 0:
#         first_sliced_list = number_list[:len(number_list) // 2:]
#         second_sliced_list = number_list[len(number_list) // 2:len(number_list):]
#         reversed_second_sliced_list = second_sliced_list[::-1]
#
#         if reversed_second_sliced_list == first_sliced_list:
#             is_palindrome = True
#     else:
#         first_sliced_list = number_list[:len(number_list) // 2:]
#         second_sliced_list = number_list[len(number_list) // 2 + 1:len(number_list):]
#         reversed_second_sliced_list = second_sliced_list[::-1]
#
#         if reversed_second_sliced_list == first_sliced_list:
#             is_palindrome = True
#     print(is_palindrome)
