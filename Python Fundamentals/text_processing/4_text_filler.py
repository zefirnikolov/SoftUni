banned_words = input().split(", ")
text = input()

for element in banned_words:
    if element in text:
        text = text.replace(element, '*' * len(element))

print(text)
