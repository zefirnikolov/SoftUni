text = input()
new_text = ''

add_to_text = ''
two_digits_counter = 0

for index in range(len(text)):
    element = text[index]

    if not element.isdigit():
        add_to_text += element
    else:
        if two_digits_counter == 1:
            two_digits_counter -= 1
            continue
        multiplier = ''
        if (index + 1) in range(len(text)):
            if text[index + 1].isdigit():
                multiplier = int(text[index] + text[index + 1])
                two_digits_counter += 1
            else:
                multiplier = int(text[index])
        else:
            multiplier = int(text[index])

        new_text += add_to_text * multiplier
        add_to_text = ''

new_text = new_text.upper()
print(f'Unique symbols used: {len(set(new_text))}')
print(new_text)
