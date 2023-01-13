phonebook = {}

while True:
    command = input()
    if command.isdigit():
        break

    action_list = command.split("-")
    name = action_list[0]
    number_phone = action_list[1]
    phonebook[name] = number_phone

command = int(command)
for i in range(command):
    search_name = input()

    if search_name in phonebook:
        print(f"{search_name} -> {phonebook[search_name]}")
        # for name, number_phone in phonebook.items():
        #     if search_name == name:
        #         print(f"{name} -> {number_phone}")
        #         break
    else:
        print(f"Contact {search_name} does not exist.")
