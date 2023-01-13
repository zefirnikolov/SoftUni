def filter_func(banned: list, data):
    for element in banned:
        if element in data:
            data = data.replace(element, '*' * len(element))
    return data


banned_words = input().split(", ")
text = input()
new_text = filter_func(banned_words, text)
print(new_text)
