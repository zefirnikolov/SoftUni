# ace two three four five six

deck_list = input("Enter the even different cards separated by a space here: ").split()
number_of_faro_shuffles_eq_loops = int(input("Enter the number of faro shuffles you want here: "))

for _ in range(number_of_faro_shuffles_eq_loops):
    left_deck = []
    right_deck = []

    for index in range(len(deck_list)):
        if index < len(deck_list) / 2:
            left_deck.append(deck_list[index])
        else:
            right_deck.append(deck_list[index])

    if _ == 0:
        print(f"Starting deck: {deck_list}")

    deck_list.clear()

    for split_index in range(len(left_deck)):
        deck_list.append(left_deck[split_index])
        deck_list.append(right_deck[split_index])

    if _ == 0:
        print(f'How the deck should look like after {_ + 1} shuffle: {deck_list}')
    else:
        print(f'How the deck should look like after {_ + 1} shuffles: {deck_list}')
