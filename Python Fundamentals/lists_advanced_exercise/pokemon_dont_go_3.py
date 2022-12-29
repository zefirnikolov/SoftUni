pokemon_list = list(map(int, input().split()))

counter = 0
while not len(pokemon_list) < 1:
    index_for_removing = int(input())

    if index_for_removing < 0:
        value_removed_eq_element = pokemon_list[0]
        pokemon_list[0] = pokemon_list[-1]
    elif index_for_removing > len(pokemon_list) - 1:
        value_removed_eq_element = pokemon_list[-1]
        pokemon_list[-1] = pokemon_list[0]
    else:
        value_removed_eq_element = pokemon_list[index_for_removing]

    counter += value_removed_eq_element

    for index in range(len(pokemon_list)):
        pokemon_eq_element = pokemon_list[index]
        if pokemon_eq_element <= value_removed_eq_element:
            pokemon_list[index] += value_removed_eq_element
        else:
            pokemon_list[index] -= value_removed_eq_element

    if index_for_removing in range(len(pokemon_list)):
        pokemon_list.pop(index_for_removing)

print(counter)
