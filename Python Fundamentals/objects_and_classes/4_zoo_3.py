class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):

        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            return f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\nTotal animals: {zoo.__animals}"
        elif species == 'fish':
            return f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\nTotal animals: {zoo.__animals}"
        elif species == 'bird':
            return f"Birds in {self.zoo_name}: {', '.join(self.birds)}\nTotal animals: {zoo.__animals}"


zoo_input = input()
zoo = Zoo(zoo_input)

number_of_loops = int(input())

for _ in range(number_of_loops):
    action_list = input().split()
    species = action_list[0]
    name = action_list[1]
    zoo.add_animal(species, name)

animal_info = input()
print(zoo.get_info(animal_info))
