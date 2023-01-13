text = input()
new_text = ''
counter = 0

for index in range(len(text)):
    element = text[index]
    if element == ">":
        counter += int(text[index + 1])
        new_text += element
    elif counter > 0:
        counter -= 1
    else:
        new_text += element
print(new_text)
