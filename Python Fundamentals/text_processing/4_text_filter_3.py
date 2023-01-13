banned_words_list = input().split(", ")
text = input()

for element in banned_words_list:
    if element in text:
        text = text.replace(element, len(element) * "*")

print(text)
