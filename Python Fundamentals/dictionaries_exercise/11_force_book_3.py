book = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    if "|" in command:
        new_list = command.split(' | ')
        force_side = new_list[0]
        user = new_list[1]
        is_in_values = False
        if not force_side in book:
            book[force_side] = []
        for value in book.values():
            if user in value:
                is_in_values = True
                break
        if is_in_values:
            continue
        else:
            book[force_side].append(user)
    if "->" in command:
        new_list = command.split(" -> ")
        force_side = new_list[1]
        user = new_list[0]
        if not force_side in book:
            book[force_side] = []
        for current_list in book.values():
            if user in current_list:
                current_list.remove(user)
                break
        book[force_side].append(user)
        print(f'{user} joins the {force_side} side!')  # possible pitfall - if the user already in the same side

for key, value in book.items():
    if len(value) == 0:
        continue
    print(f'Side: {key}, Members: {len(value)}')
    for element in value:
        print(f"! {element}")
