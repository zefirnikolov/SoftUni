text = input()
new_list = []
word = ''
for element in text:

    if element.isdigit() or element.isalpha():
        word += element
    else:
        new_list.append(word)
        word = ''
new_list.append(word)
capitals_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

total_sum = 0


for index in range(len(new_list)):
    is_not_valid = False
    element = new_list[index]
    for ind in range(len(element)):
        char = element[ind]
        if char.isdigit() or char.isalpha():
            continue
        else:
            is_not_valid = True
            break
    if element == "":
        is_not_valid = True
    if is_not_valid:
        continue
    chars_counter = 0
    letter_one = ''
    letter_last = ''
    first_action = ''
    last_action = ''
    number = ''
    for char in element:
        if char.isalpha():

            chars_counter += 1
            if chars_counter == 1:
                letter_one = char
                if char in capitals_list:
                    first_action = "divide"
                else:
                    first_action = 'multiply'
            elif chars_counter == 2:
                letter_last = char
                if char in capitals_list:
                    last_action = "subtract"
                else:
                    last_action = "add"
        else:
            number += char
    number = int(number)
    if first_action == 'divide':
        divider = 0
        for i in range(len(capitals_list)):
            if letter_one == capitals_list[i]:
                divider = i + 1
                break
        total_sum += number / divider
    elif first_action == 'multiply':
        multiplier = 0
        for i in range(len(lower_list)):
            if letter_one == lower_list[i]:
                multiplier = i + 1
        total_sum += number * multiplier
    if last_action == 'subtract':
        subtractor = 0
        for i in range(len(capitals_list)):
            if letter_last == capitals_list[i]:
                subtractor += i + 1
        total_sum -= subtractor
    elif last_action == 'add':
        adder = 0
        for i in range(len(lower_list)):
            if letter_last == lower_list[i]:
                adder += i + 1
        total_sum += adder

print(f'{total_sum:.2f}')
