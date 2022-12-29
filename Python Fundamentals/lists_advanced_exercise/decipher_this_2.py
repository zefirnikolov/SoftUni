cipher_list = input().split()

final_message = []
for element in cipher_list:
    number = ''
    current_message = ''
    for character in element:
        if character.isdigit():
            number += character
    element = element.replace(number, '')
    number = int(number)
    current_message += chr(number)
    if len(element) == 1:
        element = element[0]
    else:
        element = element[-1] + element[1:-1] + element[0]
    current_message += element
    final_message.append(current_message)

print(" ".join(final_message))
