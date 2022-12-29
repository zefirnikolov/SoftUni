gifts_list = input().split()
command_list = input().split()

while command_list != ['No', 'Money']:

    if command_list[0] == "OutOfStock":

        for i in range(len(gifts_list)):
            if gifts_list[i] == command_list[1]:
                gifts_list[i] = "None"

    elif command_list[0] == "Required":
        index = command_list[2]
        replace = command_list[1]
        if 0 < int(index) < len(gifts_list):
            gifts_list[int(index)] = replace

    elif command_list[0] == "JustInCase":
        gifts_list[-1] = command_list[1]

    command_list = input().split()

for element in gifts_list[:]:
    if element == "None":
        gifts_list.remove(element)

print(" ".join(gifts_list))
