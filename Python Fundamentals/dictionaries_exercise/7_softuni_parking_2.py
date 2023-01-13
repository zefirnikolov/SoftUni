number_of_loops = int(input())

parking = {}
for _ in range(number_of_loops):
    command = input().split()
    if command[0] == "register":
        username = command[1]
        plate_number = command[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {plate_number}")
        else:
            parking[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
    if command[0] == 'unregister':
        username = command[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

for key, value in parking.items():
    print(f"{key} => {value}")
