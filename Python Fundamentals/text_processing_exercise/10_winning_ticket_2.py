new_list = [el.strip() for el in input().split(", ")]

for index in range(len(new_list)):
    element = new_list[index]
    if len(element) != 20:
        print('invalid ticket')
        continue
    if element == "@" * 20 or element == "#" * 20 or element == "$" * 20 or element == '^' * 20:
        print(f'ticket "{element}" - 10{element[0]} Jackpot!')
        continue

    first_half = element[:10:]
    second_half = element[10:len(element):]

    counter_max = 0
    counter_max_2 = 0
    winning_symbol = ''
    char_counter = 0
    for char in first_half:
        if char == "@":
            char_counter += 1
        else:
            if char_counter > counter_max:
                counter_max = char_counter
            char_counter = 0
    if char_counter > counter_max:
        counter_max = char_counter

    for char_2 in first_half:
        if char_2 == "$":
            char_counter += 1
        else:
            if char_counter > counter_max:
                counter_max = char_counter
            char_counter = 0
    if char_counter > counter_max:
        counter_max = char_counter

    for char_3 in first_half:
        if char_3 == "#":
            char_counter += 1
        else:
            if char_counter > counter_max:
                counter_max = char_counter
            char_counter = 0
    if char_counter > counter_max:
        counter_max = char_counter

    for char_4 in first_half:
        if char_4 == "^":
            char_counter += 1
        else:
            if char_counter > counter_max:
                counter_max = char_counter
            char_counter = 0
    if char_counter > counter_max:
        counter_max = char_counter

    for char in second_half:
        if char == "@":
            char_counter += 1
        else:
            if char_counter > counter_max_2:
                counter_max_2 = char_counter
            char_counter = 0
    if char_counter > counter_max_2:
        counter_max_2 = char_counter

    for char_2 in second_half:
        if char_2 == "$":
            char_counter += 1
        else:
            if char_counter > counter_max_2:
                counter_max_2 = char_counter
            char_counter = 0
    if char_counter > counter_max_2:
        counter_max_2 = char_counter

    for char_3 in second_half:
        if char_3 == "#":
            char_counter += 1
        else:
            if char_counter > counter_max_2:
                counter_max_2 = char_counter
            char_counter = 0
    if char_counter > counter_max_2:
        counter_max_2 = char_counter

    for char_4 in second_half:
        if char_4 == "^":
            char_counter += 1
        else:
            if char_counter > counter_max_2:
                counter_max_2 = char_counter
            char_counter = 0
    if char_counter > counter_max_2:
        counter_max_2 = char_counter

    if counter_max >= 6 and counter_max_2 >= 6:
        if counter_max < counter_max_2:
            counter_max_2 = counter_max
        elif counter_max_2 < counter_max:
            counter_max = counter_max_2

        if "$" * 6 in first_half:
            winning_symbol = "$"
        elif '@' * 6 in first_half:
            winning_symbol = '@'
        elif '#' * 6 in first_half:
            winning_symbol = '#'
        elif '^' * 6 in first_half:
            winning_symbol = "^"
        print(f'ticket "{element}" - {counter_max}{winning_symbol}')
    else:
        print(f'ticket "{element}" - no match')
