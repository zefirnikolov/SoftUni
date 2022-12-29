manipulated_list = list(map(int, input().split()))

while True:
    command = input()
    if command == 'end':
        break

    action_list = command.split()
    current_action = action_list[0]

    if current_action == "exchange":
        index_slice = int(action_list[1])
        if not index_slice in range(len(manipulated_list)):
            print("Invalid index")
        else:
            first_list = manipulated_list[:index_slice + 1:]
            second_list = manipulated_list[index_slice + 1::]
            manipulated_list = second_list + first_list

    elif current_action == 'max':
        even_odd_list = []
        max_element = 0
        if action_list[1] == 'even':
            even_odd_list = [x for x in manipulated_list if x % 2 == 0]
            if not even_odd_list:
                print("No matches")
                continue
            max_element = max(even_odd_list)
        elif action_list[1] == 'odd':
            even_odd_list = [x for x in manipulated_list if x % 2 == 1]
            if not even_odd_list:
                print("No matches")
                continue
            max_element = max(even_odd_list)

        if even_odd_list.count(max_element) > 1:
            right_most_element_list = []
            for index in range(len(manipulated_list)):
                element_even_odd_list = manipulated_list[index]
                if element_even_odd_list == max_element:
                    right_most_element_list.append(index)
            print(max(right_most_element_list))
        else:
            print(manipulated_list.index(max_element))

    elif current_action == "min":
        even_odd_list = []
        min_element = 0
        if action_list[1] == 'even':
            even_odd_list = [x for x in manipulated_list if x % 2 == 0]
            if not even_odd_list:
                print("No matches")
                continue
            min_element = min(even_odd_list)
        elif action_list[1] == 'odd':
            even_odd_list = [x for x in manipulated_list if x % 2 == 1]
            if not even_odd_list:
                print("No matches")
                continue
            min_element = min(even_odd_list)

        if even_odd_list.count(min_element) > 1:
            right_most_element_list = []
            for index in range(len(manipulated_list)):
                element_even_odd_list = manipulated_list[index]
                if element_even_odd_list == min_element:
                    right_most_element_list.append(index)
            print(max(right_most_element_list))
        else:
            print(manipulated_list.index(min_element))

    elif current_action == "first":
        stop_counter = int(action_list[1])
        if stop_counter > len(manipulated_list):
            print('Invalid count')
            continue
        even_odd_list = []
        if action_list[2] == "even":
            counter = 1
            for element in manipulated_list:
                if element % 2 == 0 and counter <= stop_counter:
                    even_odd_list.append(element)
                    counter += 1
            print(even_odd_list)
        elif action_list[2] == "odd":
            counter = 1
            for element in manipulated_list:
                if element % 2 == 1 and counter <= stop_counter:
                    even_odd_list.append(element)
                    counter += 1
            print(even_odd_list)
    elif current_action == "last":
        stop_counter = int(action_list[1])
        if stop_counter > len(manipulated_list):
            print("Invalid count")
            continue
        even_odd_list = []
        if action_list[2] == "even":
            counter = 1
            for index in range(len(manipulated_list) - 1, -1, -1):
                element = manipulated_list[index]
                if element % 2 == 0 and counter <= stop_counter:
                    even_odd_list.append(element)
                    counter += 1
            print(even_odd_list[::-1])
        if action_list[2] == 'odd':
            counter = 1
            for index in range(len(manipulated_list) - 1, -1, -1):
                element = manipulated_list[index]
                if element % 2 == 1 and counter <= stop_counter:
                    even_odd_list.append(element)
                    counter += 1
            print(even_odd_list[::-1])

print(manipulated_list)
