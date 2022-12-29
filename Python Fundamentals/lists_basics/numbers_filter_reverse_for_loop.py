number_of_loops = int(input())

list_with_numbers = []

for _ in range(number_of_loops):
    current_number = int(input())
    list_with_numbers.append(current_number)

current_action = input()

if current_action == 'even':

    for i in range(len(list_with_numbers) - 1, -1, -1):
        element = list_with_numbers[i]
        if element % 2 != 0:
            list_with_numbers.remove(element)

elif current_action == 'odd':

    for i in range(len(list_with_numbers) - 1, -1, -1):
        element = list_with_numbers[i]
        if element % 2 != 1:
            list_with_numbers.remove(element)

elif current_action == 'negative':

    for i in range(len(list_with_numbers) - 1, -1, -1):
        element = list_with_numbers[i]
        if not element < 0:
            list_with_numbers.remove(element)

elif current_action == 'positive':

    for i in range(len(list_with_numbers) - 1, -1, -1):
        element = list_with_numbers[i]
        if not element >= 0:
            list_with_numbers.remove(element)

print(list_with_numbers)
