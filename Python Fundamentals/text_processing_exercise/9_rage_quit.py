text = input()
message = ""
counter = 0
digit_counter = 0
for index in range(len(text)):
    if digit_counter == 1:
        digit_counter = 0
        continue
    element = text[index]
    if element.isdigit():
        if index + 1 in range(len(text)):
            if not text[index + 1].isdigit():
                message += text[index - counter:index] * int(element)
                counter = 0
            else:
                multiplier = int(element + text[index + 1])
                digit_counter += 1
                message += text[index - counter:index] * multiplier
                counter = 0
        else:
            message += text[index - counter:index] * int(element)
            counter = 0
    else:
        counter += 1

new_list = [char.upper() for char in message]
unique_list = []
for element in new_list:
    if element in unique_list:
        continue
    else:
        unique_list.append(element)
print(f'Unique symbols used: {len(unique_list)}')
print(''.join(new_list))
