int_numbers_list = [int(x) for x in input().split(", ")]

last_list = []

for index, element in enumerate(int_numbers_list):
    if element % 2 == 0:
        last_list.append(index)

print(last_list)
