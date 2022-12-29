def hello():
    return f'Hello SoftUni'


print(hello())


def hello_enter_name(name):  # Function is not empty - it wants variable in the Parentheses
    return f"Hello {name}"


print(hello_enter_name("Gosho"))  # Inside is what the function wants, It might be input()


def person(first_name="Pesho", second_name='Gosho'):
    print(first_name, second_name)


person()
person("Pepi", 'Peshov')


def greet(name):
    return f"Hello {name}"


username = input()
print(greet(username))

full_name = lambda first, last: f"I am {first} {last}"
result = full_name("Pesho", "Peshev")
print(result)


def full_name(first, last):
    return f"I am {first} {last}"


f_name = input()
last_name = input()

print(full_name(f_name, last_name))
