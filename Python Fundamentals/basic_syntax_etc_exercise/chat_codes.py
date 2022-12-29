number_of_messages_eq_loops = int(input())

for _ in range(number_of_messages_eq_loops):
    message = int(input())

    if message == 88:
        print("Hello")

    elif message == 86:
        print("How are you?")

    elif (message != 88 or message != 86) and message < 88:
        print("GREAT!")

    elif message > 88:
        print("Bye.")
