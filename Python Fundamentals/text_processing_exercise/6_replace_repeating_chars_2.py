text = input()
new_string = ''
last_element = ''
for index in range(len(text)):
    element = text[index]
    if element == last_element:
        continue
    else:
        new_string += element

    last_element = text[index]
print(new_string)
