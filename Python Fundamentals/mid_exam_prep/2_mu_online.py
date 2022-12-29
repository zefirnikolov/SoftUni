dungeons_room = input().split("|")

health = 100
bitcoins = 0
room = 0
is_dead = False

for room_eq_element in dungeons_room:
    command_list = room_eq_element.split()
    action = command_list[0]
    room += 1
    if action == "potion":
        healing_potion = int(command_list[1])
        if health + healing_potion > 100:
            over_sum = health + healing_potion - 100
            difference = healing_potion - over_sum
            health = 100
            print(f"You healed for {difference} hp.")
        else:
            health = health + healing_potion
            print(f"You healed for {healing_potion} hp.")
        print(f"Current health: {health} hp.")
    elif action == "chest":
        bitcoins += int(command_list[1])
        print(f"You found {int(command_list[1])} bitcoins.")
    else:
        monster = command_list[0]
        damage = int(command_list[1])
        health -= damage
        if health <= 0:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room}")
            is_dead = True
            break
        else:
            print(f"You slayed {monster}.")

if not is_dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
