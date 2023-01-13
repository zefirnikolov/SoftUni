elements = input().split()
searching_items = input().split()

products_dict = {elements[i]: int(elements[i + 1]) for i in range(0, len(elements), 2)}
# products_dict = {}
# for i in range(0, len(elements), 2):
#     products_dict[elements[i]] = elements[i + 1]

for element in searching_items:
    if element in products_dict:

        for key in products_dict.keys():
            value = products_dict[key]
            if element == key:
                print(f"We have {value} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")
