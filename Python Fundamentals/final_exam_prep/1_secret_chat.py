message = input()

while True:
    command = input()
    if command == "Reveal":
        break
    action_list = command.split(":|:")
    current_action = action_list[0]
    if current_action == "InsertSpace":
        index = int(action_list[1])
        message = message[:index] + ' ' + message[index:]
        print(message)
    elif current_action == 'Reverse':
        substring = action_list[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            to_add = substring[::-1]
            message = message + to_add
            print(message)
        else:
            print('error')
    elif current_action == "ChangeAll":
        substring = action_list[1]
        replacement = action_list[2]
        message = message.replace(substring, replacement)
        print(message)
print(f"You have a new text message: {message}")
