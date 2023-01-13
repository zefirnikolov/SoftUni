number_of_loops = int(input())
piano_pieces = {}

for _ in range(number_of_loops):
    piece, composer, key = input().split("|")
    piano_pieces[piece] = {composer: key}

while True:
    command = input()
    if command == 'Stop':
        break
    action_list = command.split("|")
    current_action = action_list[0]
    piece = action_list[1]

    if current_action == 'Add':
        composer = action_list[2]
        key = action_list[3]
        if not piece in piano_pieces:
            piano_pieces[piece] = {composer: key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif current_action == "Remove":
        if piece in piano_pieces:
            print(f"Successfully removed {piece}!")
            del piano_pieces[piece]
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    elif current_action == "ChangeKey":
        if piece in piano_pieces:
            new_key = action_list[2]
            for key, value in piano_pieces.items():
                if key == piece:
                    for nested_key, nested_value in value.items():
                        piano_pieces[key][nested_key] = new_key
                        print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key, value in piano_pieces.items():

    for nested_key, nested_value in value.items():
        print(f"{key} -> Composer: {nested_key}, Key: {nested_value}")
