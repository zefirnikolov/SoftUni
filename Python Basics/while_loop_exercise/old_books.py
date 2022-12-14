book_to_find = input()
book_name = input()

counter = 0
is_there_a_book = False

while book_name != "No More Books":

    if book_name == book_to_find:
        is_there_a_book = True
        break

    counter += 1
    book_name = input()

if is_there_a_book:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
