cupids_list = list(map(int, input().split("@")))

index = 0
last_position_index = 0
while True:
    command = input()

    if command == "Love!":
        break

    action_list = command.split()

    index += int(action_list[1])
    if index not in range(len(cupids_list)):
        index = 0
    last_position_index = index
    if cupids_list[index] == 0:
        print(f"Place {index} already had Valentine's day.")
        continue
    cupids_list[index] -= 2
    if cupids_list[index] == 0:
        print(f"Place {index} has Valentine's day.")

print(f"Cupid's last position was {last_position_index}.")
if cupids_list.count(0) == len(cupids_list):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(cupids_list) - cupids_list.count(0)} places.")
