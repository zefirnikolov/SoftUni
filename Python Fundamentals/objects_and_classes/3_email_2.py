big_list = []

while True:
    command = input()
    if command == "Stop":
        break

    action_list = command.split()
    sentence = f"{action_list[0]} says to {action_list[1]}: {action_list[2]}."
    big_list.append(sentence)

new_list = list(map(int, input().split(", ")))

for index in range(len(big_list)):
    is_send = False

    for element in new_list:
        if index == element:
            is_send = True

    print(f"{big_list[index]} Sent: {is_send}")
