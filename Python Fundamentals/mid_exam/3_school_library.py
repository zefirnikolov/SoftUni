def online_book_library(data):
    while True:
        command = input()
        if command == "Done":
            break
        action_list = command.split(" | ")
        current_action = action_list[0]
        if current_action == "Add Book":
            book_name = action_list[1]
            if not book_name in data:
                data.insert(0, book_name)
        elif current_action == "Take Book":
            book_name = action_list[1]
            if book_name in data:
                data.remove(book_name)
        elif current_action == "Swap Books":
            book_1 = action_list[1]
            book_2 = action_list[2]
            if book_1 in data and book_2 in data:  # Possible Pitfall
                index_1 = data.index(book_1)
                index_2 = data.index(book_2)
                data[index_1], data[index_2] = data[index_2], data[index_1]
        elif current_action == "Insert Book":
            book_name = action_list[1]
            if not book_name in data:
                data.append(book_name)
        elif current_action == "Check Book":
            index = int(action_list[1])
            if index in range(len(data)):
                print(data[index])

    print(', '.join(data))


books_list = input().split("&")
online_book_library(books_list)
