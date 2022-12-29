def game_func(data):
    counter = 0
    is_end = False

    while True:
        if len(data) < 1:
            break

        command = input()
        if command == "end":
            is_end = True
            break

        counter += 1
        new_list = command.split()
        first_index = int(new_list[0])
        second_index = int(new_list[1])
        if first_index == second_index or not first_index in range(len(data)) or not second_index in range(len(data)):
            print('Invalid input! Adding additional elements to the board')
            additional_element = f"-{counter}a"
            data.insert(len(data) // 2, additional_element)
            data.insert(len(data) // 2, additional_element)
        elif data[first_index] == data[second_index]:  # Possible Pitfall
            element = data[first_index]
            data.remove(element)
            data.remove(element)
            print(f"Congrats! You have found matching elements - {element}!")
        elif data[first_index] != data[second_index]:
            print('Try again!')

    if is_end:
        print(f"Sorry you lose :(")
        print(' '.join(data))
    else:
        print(f"You have won in {counter} turns!")


memory_game_list = input().split()
game_func(memory_game_list)
