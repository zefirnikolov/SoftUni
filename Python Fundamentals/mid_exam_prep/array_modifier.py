numbers_list = [int(num) for num in input().split()]

while True:
    command = input()

    if command == "end":
        break

    action_list = command.split()
    current_action = action_list[0]

    if current_action == "swap":
        index_one = int(action_list[1])
        index_two = int(action_list[2])

        numbers_list[index_one], numbers_list[index_two] = numbers_list[index_two], numbers_list[index_one]
    elif current_action == "multiply":
        mply_one = int(action_list[1])
        mply_two = int(action_list[2])

        multiplication = numbers_list[mply_one] * numbers_list[mply_two]
        numbers_list[mply_one] = multiplication
    elif current_action == "decrease":
        for i in range(len(numbers_list)):
            numbers_list[i] -= 1

print(', '.join([str(num) for num in numbers_list]))
