string_to_remove = input()
word = input()

while True:
    if string_to_remove not in word:
        break

    word = word.replace(string_to_remove, "")

print(word)
