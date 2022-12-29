inventory_list = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break

    action_list = command.split(" - ")
    current_action = action_list[0]

    if current_action == "Collect":
        if not action_list[1] in inventory_list:
            inventory_list.append(action_list[1])
    elif current_action == "Drop":
        if action_list[1] in inventory_list:
            inventory_list.remove(action_list[1])
    elif current_action == "Combine Items":
        other_list = action_list[1].split(":")
        old_item = other_list[0]
        new_item = other_list[1]
        if old_item in inventory_list:
            old_item_index = inventory_list.index(old_item)
            inventory_list.insert(old_item_index + 1, new_item)
    elif current_action == "Renew":
        if action_list[1] in inventory_list:
            inventory_list.remove(action_list[1])
            inventory_list.append(action_list[1])

print(", ".join(x for x in inventory_list))
