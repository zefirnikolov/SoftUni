from math import ceil
numbers_list = [int(num) for num in input().split(", ")]

max_value = max(numbers_list)
numbers_of_loops = ceil(max_value / 10)
last_index_eq_1st_boundary = 1

for index in range(1, numbers_of_loops + 1):
    new_list = []

    for element_2 in numbers_list:
        if index == 1:
            if element_2 <= index * 10:
                new_list.append(element_2)
        elif last_index_eq_1st_boundary < element_2 <= index * 10:
            new_list.append(element_2)
    last_index_eq_1st_boundary = index * 10
    print(f"Group of {index * 10}'s: {new_list}")
