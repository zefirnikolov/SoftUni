def letter_finder(data):
    letters = ""
    for element in data:
        if element.isalpha():
            letters += element
    return letters


def digit_finder(data):
    digits = ''
    for element in data:
        if element.isdigit():
            digits += element
    return digits


def other_finder(data):
    others = ""
    for element in data:
        if 65 <= ord(element) <= 90:
            continue
        elif 97 <= ord(element) <= 122:
            continue
        elif element.isdigit():
            continue
        else:
            others += element
    return others


text = input()
digit_text = digit_finder(text)
string_text = letter_finder(text)
other_text = other_finder(text)
print(digit_text)
print(string_text)
print(other_text)
