text = input().split()
products = {}
for index in range(len(text)):
    if index % 2 == 1:
        products[text[index - 1]] = text[index]
searched_items = input().split()
for element in searched_items:
    if element in products:
        print(f"We have {int(products[element])} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")
