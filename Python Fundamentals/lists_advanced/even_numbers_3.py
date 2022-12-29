numbers = list(map(int, input().split(", ")))
even_list = map(
    lambda x: x if numbers[x] % 2 == 0 else "no",
    range(len(numbers))
)
even_indices = list(filter(lambda a: a != 'no', even_list))
print(even_indices)
