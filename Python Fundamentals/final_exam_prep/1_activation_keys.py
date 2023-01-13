key = input()


while True:
    command = input()
    if command == 'Generate':
        break
    action_list = command.split('>>>')
    current_action = action_list[0]

    if current_action == "Contains":
        subtext = action_list[1]
        if subtext in key:
            print(f"{key} contains {subtext}")
        else:
            print(f"Substring not found!")
    elif current_action == 'Flip':
        next_action = action_list[1]
        start_index = int(action_list[2])
        end_index = int(action_list[3])
        to_change = ''
        if next_action == 'Upper':
            to_change = key[start_index:end_index].upper()
        elif next_action == 'Lower':
            to_change = key[start_index:end_index].lower()
        key = key[:start_index] + to_change + key[end_index:len(key)]
        print(key)
    elif current_action == 'Slice':
        start_index = int(action_list[1])
        end_index = int(action_list[2])
        key = key[:start_index] + key[end_index:len(key)]
        print(key)
print(f'Your activation key is: {key}')
