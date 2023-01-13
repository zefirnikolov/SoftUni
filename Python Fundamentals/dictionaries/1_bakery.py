elements = input().split()
bakery = {}
for index in range(len(elements)):
    element = elements[index]
    if index % 2 == 1:
        dict_key = elements[index - 1]
        dict_value = int(element)
        bakery[dict_key] = dict_value

print(bakery)
