number_of_elements = int(input())
wagons_list = [0] * number_of_elements

while True:
    command = input()

    if command == 'End':
        break

    data_list = command.split()
    current_command = data_list[0]

    if current_command == 'add':
        people_to_add = data_list[1]
        wagons_list[-1] += int(people_to_add)
    elif current_command == 'insert':
        index = int(data_list[1])
        number_of_people = int(data_list[2])
        wagons_list[index] += number_of_people
    elif current_command == 'leave':
        index = int(data_list[1])
        number_of_people = int(data_list[2])
        wagons_list[index] -= number_of_people

print(wagons_list)
