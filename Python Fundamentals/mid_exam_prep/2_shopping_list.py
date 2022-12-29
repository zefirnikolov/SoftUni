shopping_list = input().split("!")

while True:
    command = input()

    if command == "Go Shopping!":
        break

    action_list = command.split()
    current_action = action_list[0]

    if current_action == "Urgent":
        item = action_list[1]
        if item in shopping_list:
            continue
        else:
            shopping_list.insert(0, item)
    elif current_action == "Unnecessary":
        item = action_list[1]
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            continue
    elif current_action == "Correct":
        old_item = action_list[1]
        new_item = action_list[2]
        if old_item in shopping_list:
            old_item_index = shopping_list.index(old_item)
            shopping_list[old_item_index] = new_item
        else:
            continue
    elif current_action == "Rearrange":
        item = action_list[1]
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)
        else:
            continue

print(', '.join(shopping_list))
