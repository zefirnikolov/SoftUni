def array_modifier_func(data):
    while True:
        command = input()
        if command == "end":
            break
        action_list = command.split()
        current_action = action_list[0]
        if current_action == "swap":
            index_one = int(action_list[1])
            index_two = int(action_list[2])
            data[index_one], data[index_two] = data[index_two], data[index_one]
        elif current_action == 'multiply':
            index_one = int(action_list[1])
            index_two = int(action_list[2])
            data[index_one] = data[index_one] * data[index_two]
        elif current_action == "decrease":
            for index in range(len(data)):
                data[index] -= 1
    print(", ".join(str(num) for num in data))


nums_list = list(map(int, input().split()))
array_modifier_func(nums_list)
