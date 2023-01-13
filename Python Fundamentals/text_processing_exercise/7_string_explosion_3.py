text = input()
new_text = ''
counter = 0

for index in range(len(text)):
    element = text[index]
    if element == ">":
        new_text += element
        counter += int(text[index + 1])
        continue
    if counter == 0:
        new_text += element
    else:
        counter -= 1

print(new_text)
