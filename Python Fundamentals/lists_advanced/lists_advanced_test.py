x = []
for num in range(5):
    x.append(num)

y = [num for num in range(5)]
print(x, y)


nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
squares_list = [x ** 2 for x in nums_list]
evens_list = [x for x in nums_list if x % 2 == 0]
filtered_list = [True if x % 2 == 0 else False for x in nums_list]
nested_cond_statements_list = [x for x in nums_list if x % 2 == 0 if x != 10]
nums_to_str_list = [str(x) for x in nums_list]
nums_list_back_to_int = [int(x) for x in nums_to_str_list]
print(squares_list)
print(evens_list)
print(filtered_list)
print(nested_cond_statements_list)
print(nums_to_str_list)
print(nums_list_back_to_int)

nested_list_matrix = [[x for x in range(3)] for _ in range(3)]
print()
print(nested_list_matrix)
