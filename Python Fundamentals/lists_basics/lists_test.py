# import array as arr
# test = arr.array('u', ['p', 'e', 's', 'h', 'o'])
#
# for ch in test:
#     print(ch, end='')

# import numpy as np

list_one = [5, 10, 15, 20, int, [5, 10, 15, 20], list]
print(list_one[-2])
print(type(list_one))

# for element in list_one:
#     print(element, end=" ")

for i, element in enumerate(list_one):
    print(i, element)

list_one.pop(3)
print(list_one)


print()
new_list = []

list_in_range = list(range(1, 10 + 1, + 1))  # range(1, 11) - short syntax; start = 0, end = last - 1
print(list_in_range)

if 10 in list_one:
    print('Ok')

if 555 not in list_one:
    print("double ok")

new_list.append('Pesho')
new_list.append('Gosho')
new_list.append('Johny')

print(new_list)
new_list.remove("Pesho")
new_list.pop()
print(new_list)
new_list.clear()
print(new_list)
