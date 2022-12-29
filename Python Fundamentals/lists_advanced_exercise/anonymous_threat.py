data_input_list = input().split()

while True:
    command = input()

    if command == "3:1":
        break

    rules_list = command.split()
    action = rules_list[0]

    if action == "merge":
        start_index = int(rules_list[1])
        end_index = int(rules_list[2])

        if start_index < 0:
            start_index = 0

        if len(data_input_list) - 1 > start_index:
            data_input_list[start_index:end_index + 1] = [''.join(data_input_list[start_index: end_index + 1])]
        else:
            continue

    elif action == "divide":
        divide_index = int(rules_list[1])
        divider = int(rules_list[2])

        element_for_division = data_input_list[divide_index]
        chunks, chunk_size = len(element_for_division), len(element_for_division)//divider
        chunk_list = [element_for_division[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
        if len(element_for_division) % divider != 0:
            chunk_list[divider - 1: len(chunk_list) + 1] = [''.join(chunk_list[divider - 1: len(chunk_list) + 1])]

        if element_for_division == data_input_list[-1]:
            for element in chunk_list:
                data_input_list.append(element)
            data_input_list.pop(divide_index)
        else:
            for index, element in enumerate(chunk_list):
                data_input_list.insert(divide_index + 1 + index, element)
            data_input_list.pop(divide_index)

print(' '.join(data_input_list))
