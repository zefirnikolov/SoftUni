number = int(input())

counter = 1
is_counter_bigger_than_number = False

for row in range(1, number + 1):

    for col in range(1, row + 1):
        if counter > number:
            is_counter_bigger_than_number = True
            break
        print(f'{counter}', end=" ")
        counter += 1
    if is_counter_bigger_than_number:
        break
    print()
