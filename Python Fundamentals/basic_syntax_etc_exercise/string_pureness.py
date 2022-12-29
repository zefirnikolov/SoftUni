number_of_loops = int(input())

for _ in range(number_of_loops):
    string = input()
    is_pure = True

    for char in string:
        if char == "," or char == "." or char == "_":
            is_pure = False
            break

    if is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
