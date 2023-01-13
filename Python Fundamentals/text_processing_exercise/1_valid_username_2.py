def validator(data):
    valid = True
    if len(data) < 3:
        valid = False
    if len(data) > 16:
        valid = False
    for char in data:
        if char.isalnum() or char == "-" or char == '_':
            continue
        else:
            valid = False
    return valid


print('\n'.join([ele for ele in input().split(", ") if validator(ele)]))
