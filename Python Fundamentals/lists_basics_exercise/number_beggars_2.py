values_list = input().split(", ")
count_of_beggars = int(input())

sums_list_temp = []
final_list = []

for element_1 in range(count_of_beggars):

    for element_2 in range(element_1, len(values_list), count_of_beggars):
        sums_list_temp.append(int(values_list[element_2]))

    final_list.append(sum(sums_list_temp))
    sums_list_temp.clear()

print(final_list)
