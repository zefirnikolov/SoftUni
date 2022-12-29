input_list = input().split()
count_of_numbers_to_remove_eq_loops = int(input())

input_list_as_digits = [int(i) for i in input_list]

for _ in range(count_of_numbers_to_remove_eq_loops):
    input_list_as_digits.remove(min(input_list_as_digits))

final_list = [str(i) for i in input_list_as_digits]

print(", ".join(final_list))
