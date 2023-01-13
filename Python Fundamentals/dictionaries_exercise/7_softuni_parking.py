number_of_commands = int(input())
parking = {}

for _ in range(number_of_commands):
    action_list = input().split()
    current_action = action_list[0]
    username = action_list[1]

    if current_action == 'register':
        plate_number = action_list[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {plate_number}")
        else:
            parking[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
    elif current_action == 'unregister':
        if username in parking:
            del parking[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for key, value in parking.items():
    print(f'{key} => {value}')
