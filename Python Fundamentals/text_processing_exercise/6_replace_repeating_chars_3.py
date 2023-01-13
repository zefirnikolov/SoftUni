text = input()
new_text = ''
last_element = ''
for index in range(len(text)):
    element = text[index]
    if index == len(text) - 1:
        last_element = element
        break
    if element == text[index + 1]:
        continue
    else:
        new_text += element
new_text += last_element
print(new_text)
