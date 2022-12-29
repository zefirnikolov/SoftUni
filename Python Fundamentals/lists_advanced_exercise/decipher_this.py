cipher_list = input()

ascii_number = ''
ascii_word = ''

for letter in cipher_list:
    if letter.isdigit() or letter == " ":
        ascii_number += letter
    if not letter.isdigit() or letter == " ":
        ascii_word += letter

ascii_code_list = [chr(int(x)) for x in ascii_number.split()]

word_list = ascii_word.split()
new_word_list = []
for element in word_list:
    if len(element) == 1:
        new_element = element
    else:
        new_element = element[-1:] + element[1:-1] + element[:1]
    new_word_list.append(new_element)

for i in range(len(new_word_list)):
    decipher = ascii_code_list[i] + new_word_list[i]
    print(decipher, end=" ")
