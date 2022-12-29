import timeit


def even_nums():
    even_num = []

    for num in [1, 2, 3, 4, 5, 6]:
        even_num.append(num)
    return even_num


def even_numb():
    return [num for num in [1, 2, 3, 4, 5, 6]]


print(timeit.timeit(even_numb))
print(timeit.timeit(even_nums))
