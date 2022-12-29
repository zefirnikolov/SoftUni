def is_even(x):
    if x % 2 == 0:
        return True
    # return x % 2 ==0


numbers_list = input().split()
int_numbers_list = [int(x) for x in numbers_list]
list_2 = list(filter(is_even, int_numbers_list))
# Take all the elements from int_numbers_list and check with is_even function. Fill in list only if it's true.
print(list_2)
