book = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if "|" in command:
        action_list = command.split(" | ")
        side = action_list[0]
        user = action_list[1]
        is_user = False
        for value in book.values():
            if user in value:
                is_user = True
                break
        if not is_user:
            if not side in book:
                book[side] = [user]
            else:
                book[side].append(user)

    else:
        action_list = command.split(" -> ")
        side = action_list[1]
        user = action_list[0]

        for key, value in book.items():
            if user in value:
                value.remove(user)
                break

        if not side in book:
            book[side] = [user]
        else:
            book[side].append(user)
        print(f"{user} joins the {side} side!")


for key, value in book.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for element in value:
            print(f"! {element}")
