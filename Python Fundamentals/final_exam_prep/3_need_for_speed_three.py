number_of_loops = int(input())
vehicles = {}
for _ in range(number_of_loops):
    car, mileage, fuel = input().split("|")
    vehicles[car] = [int(mileage), int(fuel)]

while True:
    command = input()
    if command == "Stop":
        break
    action_list = command.split(" : ")
    current_action = action_list[0]
    car = action_list[1]
    if current_action == 'Drive':
        distance = int(action_list[2])
        fuel = int(action_list[3])
        if vehicles[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            vehicles[car][0] += distance
            vehicles[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if vehicles[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                del vehicles[car]
    elif current_action == 'Refuel':
        fuel = int(action_list[2])
        vehicles[car][1] += fuel
        if vehicles[car][1] > 75:
            difference = vehicles[car][1] - 75
            filled_fuel = fuel - difference
            print(f"{car} refueled with {filled_fuel} liters")
            vehicles[car][1] = 75
        else:
            print(f"{car} refueled with {fuel} liters")
    elif current_action == 'Revert':
        kilometers = int(action_list[2])
        vehicles[car][0] -= kilometers
        if vehicles[car][0] < 10000:
            vehicles[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for key, value in vehicles.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
