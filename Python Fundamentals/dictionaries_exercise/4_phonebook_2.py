phonebook = {}

while True:
    command = input()
    if command.isdigit():
        break
    new_list = command.split("-")
    name = new_list[0]
    number = new_list[1]
    phonebook[name] = number

number_of_loops = int(command)
for _ in range(number_of_loops):
    searched_name = input()
    if searched_name in phonebook:
        print(f'{searched_name} -> {phonebook[searched_name]}')
    else:
        print(f'Contact {searched_name} does not exist.')
