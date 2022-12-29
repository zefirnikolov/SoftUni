list_l = [1, 2, 'g', 4]

if 4 > len(list_l) - 1:
    print('ok')


product = "1,000,000"

first, second, third = product.split(",")
value = first + second + third
print(int(value) + 1)


# list_2 = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in range(4, 2 - 1, -1):
#     list_2.pop(i)

# for index, element in reversed(list(enumerate(list_l))):
#     print(index)
#     print(element)
#
# for index in range(len(list_l) - 1, -1, -1):
#     element = list_l[index]
#     print(index, end=" ")
#     print(element, end=" ")

# old_item = "g"
# index_old_item = list_l.index(old_item)
# print(index_old_item)

# print(list_2)
#
# print(4 % 3)
#
# print(-1 * -5)
