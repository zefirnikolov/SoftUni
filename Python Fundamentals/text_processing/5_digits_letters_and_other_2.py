text = input()
digits = ''
letters = ''
others = ''

for element in text:
    if element.isdigit():
        digits += element
    elif element.isalpha():
        letters += element
    elif not element.isalnum():
        others += element

print(digits)
print(letters)
print(others)
