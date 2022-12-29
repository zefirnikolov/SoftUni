initial_string = input()

numbers_list = []
non_numbers_list = []
for letter in initial_string:
    if letter.isdigit():
        numbers_list.append(int(letter))
    else:
        non_numbers_list.append(letter)

take_list = []
skip_list = []
for index in range(len(numbers_list)):
    ele = numbers_list[index]
    if index % 2 == 0:
        take_list.append(ele)
    else:
        skip_list.append(ele)

non_numbers_string = ''.join(non_numbers_list)
taken_string = ''
skipped_string = ''

for (element_1, element_2) in zip(take_list, skip_list):
    if element_1 != 0:
        taken_string += non_numbers_string[:element_1:]
        non_numbers_string = non_numbers_string[element_1::]

    if element_2 != 0:
        skipped_string += non_numbers_string[:element_2:]
        non_numbers_string = non_numbers_string[element_2::]

print(taken_string)
