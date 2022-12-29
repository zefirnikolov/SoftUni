def shoot(target_seq_list):
    shot_counter = 0

    while True:
        command = input()
        if command == "End":
            break

        shot_index = int(command)

        if shot_index in range(len(target_seq_list)):

            if target_seq_list[shot_index] == -1:
                continue

            shoot_value = target_seq_list[shot_index]
            target_seq_list[shot_index] = -1
            shot_counter += 1
            for index in range(len(target_seq_list)):
                element = target_seq_list[index]
                if element == -1:
                    continue
                else:
                    if element > shoot_value:
                        target_seq_list[index] -= shoot_value
                    else:
                        target_seq_list[index] += shoot_value

    print(f"Shot targets: {shot_counter} -> {' '.join([str(x) for x in target_seq_list])}")


data = list(map(int, input().split()))
shoot(data)
