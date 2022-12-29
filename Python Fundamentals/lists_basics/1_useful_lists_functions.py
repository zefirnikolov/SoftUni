my_list = [1, 2, 3, 4, 5, 2, 2, 8, "tralala", 9, 10]

print(my_list)

# If I use for in range(list/string) - I work with the element.
# If I use for in range(len(list/string)) I work with index
# Most of the time it's better to use range(len(list/str)) because element = list[index]

# List scrapping from last to 1st element:
# removing elements from the list with pop. Will remove all elements. It can't remove properly with forward for loop!
for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i], end=" ")

print()
new_list = my_list.copy()
for index in range(len(new_list) - 1, -1, -1):
    # element = new_list[index]
    # new_list.remove(element)
    new_list.pop(index)
    print(new_list)

# my_list.sort(reverse=True)
# print(my_list)


# print(my_list.pop(0))
# print(my_list)
#
# my_list.insert(5, "Gosho")
# print(my_list)
# print(my_list.remove("Gosho"))
# print(my_list.pop("Gosho"))
# print(my_list)

# print(my_list)
# my_list.remove(5)
# print(my_list)

# number = my_list.index("tralala")
# print(number)
#
# repetition = my_list.count(22)
# print(repetition)

# print(my_list)
# # my_list.reverse()
# print(my_list[::-1])
# print(my_list)
# #
# del my_list[3]
# print(my_list)

# my_list.append("Gosho")
# print(my_list)

list_2 = []
#
list_2.append(my_list.pop())
print(my_list)
print(list_2)
removed_pop = my_list.pop()
print(removed_pop)

# Swap: 3 - tralala
# Find index
index_one = my_list.index(3)  # find on which index is the Value 3
index_two = my_list.index("tralala")  # find on which index is the tralala. They should exist
my_list[index_one], my_list[index_two] = my_list[index_two], my_list[index_one]
print(my_list)

# some_input = "1, 2, 3, 4, 5"
# created_list = some_input.split(", ")
# print(created_list)
#
# # list_2 = my_list.copy()
#
# created_list_int = []
# for element in created_list:
#     created_list_int.append(int(element))
#
# sum_created_list_int = sum(created_list_int)
# print(sum_created_list_int)
