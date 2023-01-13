def reverser(data: str):
    data_reversed = data[::-1]
    return data_reversed


while True:
    command = input()

    if command == "end":
        break

    string_reversed = reverser(command)
    print(f"{command} = {string_reversed}")
