def comp_store(orders: list):

    for element in orders:
        if element < 0:
            print('Invalid price!')
        orders.remove(element)


command_list = []
while True:
    command_input = input()
    command_list.append(command_input)
    if command_input == "special" or command_input == 'regular':
        break
