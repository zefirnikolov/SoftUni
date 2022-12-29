number_of_loops = int(input())

list_with_numbers = []
filtered_list = []

for _ in range(number_of_loops):
    current_number = int(input())
    list_with_numbers.append(current_number)

current_action = input()

if current_action == 'even':

    for element in list_with_numbers:

        if element % 2 == 0:
            filtered_list.append(element)

elif current_action == 'odd':

    for element in list_with_numbers:

        if element % 2 == 1:
            filtered_list.append(element)

elif current_action == 'negative':

    for element in list_with_numbers:

        if element < 0:
            filtered_list.append(element)

elif current_action == 'positive':

    for element in list_with_numbers:

        if element >= 0:
            filtered_list.append(element)

print(filtered_list)
