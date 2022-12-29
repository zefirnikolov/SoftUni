factor = int(input())
number_of_multiples_eq_loops = int(input())

numbers_list = []

for element in range(1, number_of_multiples_eq_loops + 1):
    multiple = element * factor
    numbers_list.append(multiple)

print(numbers_list)
