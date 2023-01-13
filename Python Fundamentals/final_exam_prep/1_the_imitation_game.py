text = input()

while True:
    command = input()
    if command == 'Decode':
        break
    action_list = command.split("|")
    current_action = action_list[0]

    if current_action == "Move":
        slice_index = int(action_list[1])
        move = text[:slice_index:]
        text = text[slice_index:len(text)]
        text = text + move
    elif current_action == "Insert":
        index = int(action_list[1])
        value = action_list[2]
        text = text[:index] + value + text[index:len(text)]
    elif current_action == 'ChangeAll':
        substring = action_list[1]
        replacement = action_list[2]
        text = text.replace(substring, replacement)
print(f"The decrypted message is: {text}")
