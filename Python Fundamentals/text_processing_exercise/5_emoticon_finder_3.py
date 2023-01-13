text = input()
symbols = []

for index in range(len(text)):
    element = text[index]
    if element == ":":
        symbols.append(element + text[index + 1])
for ele in symbols:
    print(ele)
