import re

number_of_loops = int(input())
search_pattern = r'(^|(?<=\s))(\$|\%)([A-Z][a-z]{2,})\2\:\s(\[\d+\]\|)(\[\d+\]\|)(\[\d+\]\|)($|(?=\s))'

for _ in range(number_of_loops):
    text = input()
    result = re.findall(search_pattern, text)
    if result:
        tag = result[0][2]
        letter_1 = result[0][3]
        letter_1 = int(letter_1[1:len(letter_1) - 2])
        letter_2 = result[0][4]
        letter_2 = int(letter_2[1:len(letter_2) - 2])
        letter_3 = result[0][5]
        letter_3 = int(letter_3[1:len(letter_3) - 2])
        decrypted_message = chr(letter_1) + chr(letter_2) + chr(letter_3)
        print(f"{tag}: {decrypted_message}")
    else:
        print("Valid message not found!")
