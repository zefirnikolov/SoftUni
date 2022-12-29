targets_list = [int(target) for target in input().split()]

# shot_list = []
# shot_counter = 0

while True:
    command = input()

    if command == "End":
        break

    shot_index = int(command)

    if shot_index in range(len(targets_list)):

        # shot_counter += 1

        # if shot_index <= -1:
        #     continue

        # if shot_index in shot_list:
        #     continue
        # shot_list.append(shot_index)


        # if targets_list[shot_index] == -1:
        #     continue

        if targets_list[shot_index] == targets_list[-1]:
            targets_list.append(-1)
        else:
            targets_list.insert(shot_index + 1, -1)

        removed_pop = targets_list.pop(shot_index)
        for index, current_target in enumerate(targets_list):
            if current_target == -1:
                continue
            if index == shot_index:
                continue
            elif current_target > removed_pop:
                targets_list[index] -= removed_pop
            elif current_target <= removed_pop:
                targets_list[index] += removed_pop

shot_targets = targets_list.count(-1)

print(f"Shot targets: {shot_targets} -> {' '.join([str(target) for target in targets_list])}")
