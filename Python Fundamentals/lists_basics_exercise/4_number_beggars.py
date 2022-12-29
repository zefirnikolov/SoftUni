values_list = list(map(int, input().split(", ")))
number_of_beggars = int(input())
beggars_list = [0] * number_of_beggars

for index, element in enumerate(beggars_list):

    for index_2 in range(index, len(values_list), number_of_beggars):

        beggars_list[index] += values_list[index_2]

print(beggars_list)
