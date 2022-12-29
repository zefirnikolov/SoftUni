pokemon_list = list(map(int, input().split()))

counter = 0
while not len(pokemon_list) < 1:
    index_for_removing = int(input())

    if index_for_removing < 0:
        value_pop_eq_element = pokemon_list.pop(0)
        pokemon_list.insert(0, pokemon_list[-1])
        counter += value_pop_eq_element
    elif index_for_removing > len(pokemon_list) - 1:
        value_pop_eq_element = pokemon_list.pop(-1)
        pokemon_list.append(pokemon_list[0])
        counter += value_pop_eq_element
    else:  # value_pop_eq_element in range(len(pokemon_list))
        value_pop_eq_element = pokemon_list.pop(index_for_removing)
        counter += value_pop_eq_element

    for index in range(len(pokemon_list)):
        pokemon_eq_element = pokemon_list[index]
        if pokemon_eq_element <= value_pop_eq_element:
            pokemon_list[index] += value_pop_eq_element
        else:
            pokemon_list[index] -= value_pop_eq_element

print(counter)
