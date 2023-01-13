text = input().split()

bakery = {}
for index in range(len(text)):
    element = text[index]

    if index % 2 == 1:
        bakery[text[index - 1]] = int(element)

print(bakery)
