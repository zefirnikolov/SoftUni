values_list = input().split(", ")
count_of_beggars = int(input())

final_list = []
counter_of_index = 0
# values_list_as_digits = [int(i) for i in values_list]
values_list_as_digits = []

for element in values_list:
    values_list_as_digits.append(int(element))

while counter_of_index < count_of_beggars:
    current_beggar_sum = 0

    for current_index in range(counter_of_index, len(values_list_as_digits), count_of_beggars):
        current_beggar_sum += values_list_as_digits[current_index]

    counter_of_index += 1
    final_list.append(current_beggar_sum)

print(final_list)
