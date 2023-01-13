new_list = [text for text in input().split(" ") if not text == '']
total_sum = 0

for index in range(len(new_list)):
    element = new_list[index]
    current_sum = 0
    number = ''
    first_letter = element[0]
    last_letter = element[-1]
    for i in range(len(element)):
        char = element[i]
        if i == 0:
            continue
        if i != len(element) - 1:
            number += char
        else:
            number = int(number)
            if first_letter.isupper():
                divider = 0
                for position in range(ord("A"), ord("Z") + 1):
                    if first_letter == chr(position):
                        divider = ord(first_letter) - 64
                        break
                current_sum += number / divider
            elif first_letter.islower():
                multiplier = 0
                for position in range(ord('a'), ord('z') + 1):
                    if first_letter == chr(position):
                        multiplier = ord(first_letter) - 96
                        break
                current_sum += number * multiplier
            if last_letter.isupper():
                subtractor = 0
                for position in range(ord("A"), ord("Z") + 1):
                    if last_letter == chr(position):
                        subtractor = ord(last_letter) - 64
                        break
                current_sum -= subtractor
            elif last_letter.islower():
                adder = 0
                for position in range(ord('a'), ord('z') + 1):
                    if last_letter == chr(position):
                        adder = ord(last_letter) - 96
                        break
                current_sum += adder
            total_sum += current_sum

print(f"{total_sum:.2f}")
