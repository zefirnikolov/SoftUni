gifts_list = input().split()
command_list = input()

while not command_list == "No Money":
    command_list = command_list.split()

    if "OutOfStock" in command_list:
        for i in range(len(gifts_list)):
            if command_list[1] in gifts_list[i]:
                gifts_list[i] = "None"

    elif "Required" in command_list:
        for i in range(len(gifts_list)):
            if i == int(command_list[2]):
                gifts_list[i] = command_list[1]

    elif "JustInCase" in command_list:
        gifts_list[-1] = command_list[1]
    command_list = input()

while "None" in gifts_list:
    gifts_list.remove("None")

for i in gifts_list:
    print(i, end=" ")
