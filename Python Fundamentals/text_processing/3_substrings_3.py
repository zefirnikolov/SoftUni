to_remove = input()
text = input()

while True:
    if to_remove not in text:
        break

    text = text.replace(to_remove, "")

print(text)
