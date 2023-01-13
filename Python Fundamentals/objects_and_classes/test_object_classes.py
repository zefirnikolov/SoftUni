class Person(object):
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def say_hello(self):
        return f'Hello {self.first_name} {self.last_name}, {self.age} years old.'


ivan = Person('Ivan', 'Ivanov', 5)
print(ivan.say_hello())

print(ivan.first_name)
print(type(Person))
print(type(ivan))
print(type(ivan.first_name))
ivan.age += 1
print(ivan.age)
ivan.first_name = "Pesho"
print(ivan.first_name)
