starting_text = input()
new_text = ""

for element in starting_text:
    char_ascii = ord(element)
    new_text += chr(char_ascii + 3)

print(new_text)
