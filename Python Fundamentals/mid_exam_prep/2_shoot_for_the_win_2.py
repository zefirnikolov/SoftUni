targets_list = [int(x) for x in input().split()]

counter = 0
while True:
    command = input()
    if command == "End":
        print(f"Shot targets: {counter} -> {' '.join([str(target) for target in targets_list])}")
        break

    shot_index = int(command)

    if shot_index in range(len(targets_list)):
        current_target = targets_list[shot_index]

        for index, element in enumerate(targets_list):
            if element != -1:
                if element > current_target:
                    targets_list[index] -= current_target
                else:
                    targets_list[index] += current_target
        targets_list[shot_index] = -1
        counter += 1
