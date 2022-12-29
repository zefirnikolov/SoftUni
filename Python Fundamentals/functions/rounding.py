def rounder(numbers):
    new_list = numbers.split()
    rounded_list = []
    for element in new_list:
        rounded_float = round(float(element))
        rounded_list.append(rounded_float)
    return rounded_list


number_input = input()
print(rounder(number_input))


# numbers = input()
#
# new_list = numbers.split()
# rounded_list = []
# for element in new_list:
#     rounded_float = round(float(element))
#     rounded_list.append(rounded_float)
#
# print(rounded_list)
