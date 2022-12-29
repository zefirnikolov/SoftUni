pokemons_list = [int(num) for num in input().split()]

total_pokemon_value = 0

while not len(pokemons_list) < 1:
    input_index = int(input())
    if input_index < 0:
        removed_pop = pokemons_list.pop(0)
        pokemons_list.insert(0, pokemons_list[-1])
        total_pokemon_value += removed_pop
        for index, element in enumerate(pokemons_list):
            if element <= removed_pop:
                pokemons_list[index] += removed_pop
            else:
                pokemons_list[index] -= removed_pop
    elif input_index > len(pokemons_list) - 1:
        removed_pop = pokemons_list.pop()
        pokemons_list.append(pokemons_list[0])
        total_pokemon_value += removed_pop
        for index, element in enumerate(pokemons_list):
            if element <= removed_pop:
                pokemons_list[index] += removed_pop
            else:
                pokemons_list[index] -= removed_pop
    else:
        removed_pop = pokemons_list.pop(input_index)
        total_pokemon_value += removed_pop
        for index, element in enumerate(pokemons_list):
            if element <= removed_pop:
                pokemons_list[index] += removed_pop
            else:
                pokemons_list[index] -= removed_pop

print(total_pokemon_value)
