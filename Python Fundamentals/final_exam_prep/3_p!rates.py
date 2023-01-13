pirates = {}

while True:
    command = input()
    if command == 'Sail':
        break
    city, population, gold = command.split("||")
    if not city in pirates:
        pirates[city] = [int(population), int(gold)]
    else:
        pirates[city][0] += int(population)
        pirates[city][1] += int(gold)

while True:
    command = input()
    if command == 'End':
        break
    action_list = command.split('=>')
    current_action = action_list[0]
    if current_action == 'Plunder':
        town = action_list[1]
        people = int(action_list[2])
        gold = int(action_list[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        pirates[town][0] -= people
        pirates[town][1] -= gold
        if pirates[town][0] == 0 or pirates[town][1] == 0:
            print(f'{town} has been wiped off the map!')
            del pirates[town]
    elif current_action == 'Prosper':
        town = action_list[1]
        gold = int(action_list[2])
        if gold < 0:
            print('Gold added cannot be a negative number!')
            continue
        pirates[town][1] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {pirates[town][1]} gold.")
if not pirates:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(pirates)} wealthy settlements to go to:")
    for key, value in pirates.items():
        print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')
