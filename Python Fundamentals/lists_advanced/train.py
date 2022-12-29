number_of_elements = int(input())

train_list = []
for _ in range(number_of_elements):
    train_list.append(int(0))

command_list = input().split()

while command_list != ["End"]:
    index_value = 0
    action = 0

    if command_list[0] == "add":
        train_list[-1] += int(command_list[1])
    elif command_list[0] == "insert":

        for index, element in enumerate(command_list):
            if index == 1:
                index_value = element
            if index == 2:
                action = element
        train_list[int(index_value)] += int(action)
    elif command_list[0] == 'leave':

        for index, element in enumerate(command_list):
            if index == 1:
                index_value = int(element)
            if index == 2:
                action = int(element)
        train_list[index_value] -= action

    command_list = input().split()

print(train_list)
