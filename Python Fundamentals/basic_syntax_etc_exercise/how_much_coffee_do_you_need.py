event = input()

coffee_counter = 0

while event != 'END':

    if event == "coding" or event == 'dog' or event == 'cat' or event == 'movie':
        coffee_counter += 1

    if event == 'CODING' or event == 'DOG' or event == 'CAT' or event == 'MOVIE':
        coffee_counter += 2

    event = input()

if coffee_counter > 5:
    print('You need extra sleep')
else:
    print(coffee_counter)
