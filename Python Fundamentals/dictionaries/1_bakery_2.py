bakery_list = input().split()
key_list = []
value_list = []

for element in bakery_list:
    if element.isdigit():
        value_list.append(int(element))
    else:
        key_list.append(element)

new_dict = dict(zip(key_list, value_list))
print(new_dict)
