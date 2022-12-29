integer_list = [int(num) for num in input().split(", ")]

for index in range(len(integer_list)):
    element = integer_list[index]

    if element == 0:
        integer_list.remove(element)
        integer_list.append(0)

print(integer_list)
