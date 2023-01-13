elements = input().split()
searching_items = input().split()

products_dict = {}
for index in range(len(elements)):
    element = elements[index]
    if index % 2 == 1:
        dict_key = elements[index - 1]
        dict_value = int(element)
        products_dict[dict_key] = dict_value

for element_eq_key in searching_items:
    if element_eq_key in products_dict:
        value = products_dict[element_eq_key]
        print(f"We have {value} of {element_eq_key} left")
    else:
        print(f"Sorry, we don't have {element_eq_key}")
