world_tour = input()

while True:
    command = input()
    if command == "Travel":
        break
    action_list = command.split(':')
    current_action = action_list[0]
    if current_action == 'Add Stop':
        index = int(action_list[1])
        string = action_list[2]
        if index in range(len(world_tour)):
            world_tour = world_tour[:index] + string + world_tour[index:]
    elif current_action == "Remove Stop":
        start_index = int(action_list[1])
        end_index = int(action_list[2])
        if start_index in range(len(world_tour)) and end_index in range(len(world_tour)):
            world_tour = world_tour[:start_index] + world_tour[end_index + 1:]
    elif current_action == "Switch":
        old_string = action_list[1]
        new_string = action_list[2]
        if old_string in world_tour:
            world_tour = world_tour.replace(old_string, new_string)

    print(world_tour)
print(f"Ready for world tour! Planned stops: {world_tour}")
