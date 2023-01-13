password = input()


while True:
    command = input()
    if command == "Done":
        break

    action_list = command.split()
    current_action = action_list[0]
    new_password = ''
    if current_action == "TakeOdd":
        for index in range(len(password)):
            if index % 2 == 1:
                new_password += password[index]

        password = new_password
        print(password)
    elif current_action == "Cut":
        index = int(action_list[1])
        length = int(action_list[2])
        to_remove = password[index:index + length]
        password = password.replace(to_remove, "", 1)
        print(password)
    elif current_action == 'Substitute':
        substring = action_list[1]
        substitute = action_list[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
print(f"Your password is: {password}")
