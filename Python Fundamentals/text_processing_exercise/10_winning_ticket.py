new_list = [text.strip() for text in input().split(', ') if not text == ""]

for index in range(len(new_list)):
    element = new_list[index]
    if element == "$" * 20 or element == '#' * 20 or element == '@' * 20 or element == '^' * 20:
        print(f'ticket "{element}" - 10{element[0]} Jackpot!')
        continue
    if not len(element) == 20:
        print('invalid ticket')
        continue
    first_part = element[:len(element)//2]
    second_part = element[len(element)//2::]
    if "$" * 6 in first_part and "$" * 6 in second_part:
        max_count = 0
        other_max_count = 0
        counter = 0
        another_counter = 0
        char = ''
        char_2 = ''
        for i in range(len(first_part)):
            char = first_part[i]
            if char == "$":
                counter += 1
            else:
                if counter > max_count:
                    max_count = counter
                counter = 0
        if char == '$':
            if counter > max_count:
                max_count = counter

        for i in range(len(second_part)):
            char_2 = second_part[i]
            if char_2 == "$":
                another_counter += 1
            else:
                if another_counter > other_max_count:
                    other_max_count = another_counter
                another_counter = 0
        if char_2 == "$":
            if another_counter > other_max_count:
                other_max_count = another_counter

        if max_count <= other_max_count:
            print(f'ticket "{element}" - {max_count}$')
        else:
            print(f'ticket "{element}" - {other_max_count}$')

    elif '#' * 6 in first_part and '#' * 6 in second_part:
        max_count = 0
        other_max_count = 0
        counter = 0
        another_counter = 0
        char = ''
        char_2 = ''
        for i in range(len(first_part)):
            char = first_part[i]
            if char == "#":
                counter += 1
            else:
                if counter > max_count:
                    max_count = counter
                counter = 0
        if char == '#':
            if counter > max_count:
                max_count = counter

        for i in range(len(second_part)):
            char_2 = second_part[i]
            if char_2 == "#":
                another_counter += 1
            else:
                if another_counter > other_max_count:
                    other_max_count = another_counter
                another_counter = 0
        if char_2 == "#":
            if another_counter > other_max_count:
                other_max_count = another_counter

        if max_count <= other_max_count:
            print(f'ticket "{element}" - {max_count}#')
        else:
            print(f'ticket "{element}" - {other_max_count}#')
    elif '@' * 6 in first_part and '@' * 6 in second_part:
        max_count = 0
        other_max_count = 0
        counter = 0
        another_counter = 0
        char = ''
        char_2 = ''
        for i in range(len(first_part)):
            char = first_part[i]
            if char == "@":
                counter += 1
            else:
                if counter > max_count:
                    max_count = counter
                counter = 0
        if char == '@':
            if counter > max_count:
                max_count = counter

        for i in range(len(second_part)):
            char_2 = second_part[i]
            if char_2 == "@":
                another_counter += 1
            else:
                if another_counter > other_max_count:
                    other_max_count = another_counter
                another_counter = 0
        if char_2 == "@":
            if another_counter > other_max_count:
                other_max_count = another_counter

        if max_count <= other_max_count:
            print(f'ticket "{element}" - {max_count}@')
        else:
            print(f'ticket "{element}" - {other_max_count}@')
    elif '^' * 6 in first_part and '^' * 6 in second_part:
        max_count = 0
        other_max_count = 0
        counter = 0
        another_counter = 0
        char = ''
        char_2 = ''
        for i in range(len(first_part)):
            char = first_part[i]
            if char == "^":
                counter += 1
            else:
                if counter > max_count:
                    max_count = counter
                counter = 0
        if char == '^':
            if counter > max_count:
                max_count = counter

        for i in range(len(second_part)):
            char_2 = second_part[i]
            if char_2 == "^":
                another_counter += 1
            else:
                if another_counter > other_max_count:
                    other_max_count = another_counter
                another_counter = 0
        if char_2 == "^":
            if another_counter > other_max_count:
                other_max_count = another_counter

        if max_count <= other_max_count:
            print(f'ticket "{element}" - {max_count}^')
        else:
            print(f'ticket "{element}" - {other_max_count}^')
    else:
        print(f'ticket "{element}" - no match')
