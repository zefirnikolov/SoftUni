class Animal:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def all(self):
        return f"name: {self.name}, age: {self.age}"


persons_list = []
person = Animal("Pesho", 16)
persons_list.append(person)
print(persons_list)
player = Animal("Gosho", 18)
persons_list.append(player)
print(persons_list)
print(person.name)
print(person.species)

print(person.all())
