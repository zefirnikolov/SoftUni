number_of_loops = int(input())

list_with_numbers = []
even_list = []
odd_list = []
negative_list = []
positive_list = []

for _ in range(number_of_loops):
    current_number = int(input())
    list_with_numbers.append(current_number)

current_action = input()

if current_action == 'even':

    for element in list_with_numbers:

        if element % 2 == 0:
            even_list.append(element)

    print(even_list)

elif current_action == 'odd':

    for element in list_with_numbers:

        if element % 2 == 1:
            odd_list.append(element)
    print(odd_list)

elif current_action == 'negative':

    for element in list_with_numbers:

        if element < 0:
            negative_list.append(element)

    print(negative_list)

elif current_action == 'positive':

    for element in list_with_numbers:

        if element >= 0:
            positive_list.append(element)
    print(positive_list)
