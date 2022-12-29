first_list = input().split(", ")
second_list = input().split(", ")

last_list = []

for element in first_list:

    for element_2 in second_list:

        if element in element_2:
            last_list.append(element)
            break

print(last_list)
