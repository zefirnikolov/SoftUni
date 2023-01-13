text = input()
last_element = ''
for index in range(len(text) - 1, -1, -1):
    element = text[index]
    if element == last_element:
        text = text[:index:] + text[index + 1::]

    last_element = text[index]

print(text)
