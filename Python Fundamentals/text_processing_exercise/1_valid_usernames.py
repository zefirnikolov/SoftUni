def validator(data):
    is_valid = True
    if 3 <= len(data) <= 16:
        pass
    else:
        is_valid = False
    for element in data:
        if element.isdigit():
            continue
        elif element.isalpha():
            continue
        elif element == '-' or element == '_':
            continue
        else:
            is_valid = False
    return is_valid


text_list = input().split(", ")
for word in text_list:
    is_element_ok = validator(word)
    if is_element_ok:
        print(word)
