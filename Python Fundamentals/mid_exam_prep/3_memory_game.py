initial_list = input().split()

moves_counter = 0
is_won = False

while True:
    command = input()

    if command == 'end':
        break

    moves_counter += 1

    command_list = command.split()

    index_one = int(command_list[0])
    index_two = int(command_list[1])

    if index_one == index_two or index_one < 0 or index_two < 0 \
            or index_one > len(initial_list) - 1 or index_two > len(initial_list) - 1:
        print("Invalid input! Adding additional elements to the board")
        invalid_input_element = f'-{moves_counter}a'
        initial_list.insert(len(initial_list) // 2, invalid_input_element)
        initial_list.insert(len(initial_list) // 2, invalid_input_element)
    else:
        if initial_list[index_one] == initial_list[index_two]:
            matched_element = initial_list[index_one]
            print(f"Congrats! You have found matching elements - {initial_list[index_one]}!")
            initial_list.remove(matched_element)
            initial_list.remove(matched_element)
        else:
            print("Try again!")

    if len(initial_list) == 0:
        is_won = True
        break

if is_won:
    print(f"You have won in {moves_counter} turns!")
else:
    print("Sorry you lose :(")
    print(' '.join(initial_list))
