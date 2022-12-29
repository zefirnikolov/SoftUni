targets_list = list(map(int, input().split()))

while True:
    command = input()

    if command == "End":
        break

    action_list = command.split()
    current_action = action_list[0]

    if current_action == "Shoot":
        shoot_index = int(action_list[1])
        power_value = int(action_list[2])

        if shoot_index in range(len(targets_list)):
            targets_list[shoot_index] -= power_value

            if targets_list[shoot_index] <= 0:
                targets_list.pop(shoot_index)
    elif current_action == "Add":
        insert_index = int(action_list[1])
        value_to_insert = int(action_list[2])

        if not insert_index in range(len(targets_list)):
            print("Invalid placement!")
        else:
            targets_list.insert(insert_index, value_to_insert)
    elif current_action == "Strike":
        strike_index = int(action_list[1])
        radius = int(action_list[2])

        index_check_down = strike_index - radius
        index_check_up = strike_index + radius

        if (not index_check_down in range(len(targets_list))) or (not index_check_up in range(len(targets_list))):
            print('Strike missed!')
        else:
            for element_eq_index_check_up_and_down in range(index_check_up, index_check_down - 1, -1):
                targets_list.pop(element_eq_index_check_up_and_down)

print('|'.join([str(x) for x in targets_list]))
