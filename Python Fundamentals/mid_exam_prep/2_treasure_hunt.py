def treasure_func(data):
    while True:
        command = input()
        if command == "Yohoho!":
            break
        action_list = command.split()
        current_action = action_list[0]
        if current_action == "Loot":
            for index in range(len(action_list)):
                element = action_list[index]
                if index == 0:
                    continue
                if element in data:
                    continue
                data.insert(0, element)
        if current_action == "Drop":
            index = int(action_list[1])
            if index in range(len(data)):
                item = data[index]
                data.pop(index)
                data.append(item)
        if current_action == "Steal":
            steal_count = int(action_list[1])
            if steal_count <= 0:
                continue
            removed_list = []
            for index in range(len(data) - 1, -1, -1):
                removed_list.append(data.pop())
                steal_count -= 1
                if steal_count == 0:
                    break
            removed_list = removed_list[::-1]
            print(", ".join(item for item in removed_list))

    if not data:
        print("Failed treasure hunt.")
    else:
        plunder_counter = 0
        for element in data:
            plunder_counter += len(element)

        average_treasure_gain = plunder_counter / len(data)
        print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")


treasure_list = [item for item in input().split("|")]
treasure_func(treasure_list)
