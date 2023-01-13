def friend_maintenance(data):
    while True:
        command = input()
        if command == "Report":
            break
        action_list = command.split()
        current_action = action_list[0]
        if current_action == "Blacklist":
            name = action_list[1]
            if name in data:
                print(f"{name} was blacklisted.")
                index_name = data.index(name)
                data[index_name] = 'Blacklisted'
            else:
                print(f"{name} was not found.")
        if current_action == "Error":
            index = int(action_list[1])
            if index in range(len(data)):
                if data[index] != 'Blacklisted' and data[index] != 'Lost':
                    name = data[index]
                    print(f"{name} was lost due to an error.")
                    data[index] = "Lost"
        if current_action == "Change":
            index = int(action_list[1])
            new_name = action_list[2]
            if index in range(len(data)):
                name = data[index]
                print(f"{name} changed his username to {new_name}.")
                data[index] = new_name

    print(f"Blacklisted names: {data.count('Blacklisted')}")
    print(f"Lost names: {data.count('Lost')}")
    print(' '.join(data))


names_list = input().split(", ")
friend_maintenance(names_list)
