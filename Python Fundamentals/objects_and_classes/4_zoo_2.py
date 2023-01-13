zoo_name = input()
number_of_loops_eq_animals = int(input())

mammals = []
fishes = []
birds = []

counter = 0

for _ in range(number_of_loops_eq_animals):

    action_list = input().split()
    species = action_list[0]
    animal = action_list[1]
    counter += 1
    if species == "mammal":
        mammals.append(animal)
    elif species == "fish":
        fishes.append(animal)
    elif species == "bird":
        birds.append(animal)

type_of_animal_info = input()

if type_of_animal_info == "mammal":
    print(f"Mammals in {zoo_name}: {', '.join([animal for animal in mammals])}")
    print(f"Total animals: {counter}")
elif type_of_animal_info == "fish":
    print(f"Fishes in {zoo_name}: {', '.join([animal for animal in fishes])}\nTotal animals: {counter}")
elif type_of_animal_info == "bird":
    print(f"Birds in {zoo_name}: {', '.join([animal for animal in birds])}\nTotal animals: {counter}")
