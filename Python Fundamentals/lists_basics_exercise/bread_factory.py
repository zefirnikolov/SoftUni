# order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000
values = input().split("|")

energy = 100
coins = 100
is_closed = False

for element_out in values:
    new_list = element_out.split("-")
    type_of_item = ''
    gained_energy = 0
    last_gained_energy = 0

    if new_list[0] == "rest":
        energy += int(new_list[1])
        if energy > 100:
            gained_energy = energy
            gained_energy -= 100
            last_gained_energy = int(new_list[1]) - gained_energy
            energy = 100
            print(f"You gained {last_gained_energy} energy.")
        else:
            print(f"You gained {int(new_list[1])} energy.")
        print(f"Current energy: {energy}.")
    elif new_list[0] == 'order':
        energy -= 30
        if energy < 0:
            energy += 30
            energy += 50
            print("You had to rest!")
            continue
        else:
            coins += int(new_list[1])
            print(f"You earned {int(new_list[1])} coins.")
    elif new_list[0] != 'rest' and new_list[0] != 'order':
        coins -= int(new_list[1])
        if coins >= 0:
            print(f"You bought {new_list[0]}.")
        else:
            print(f"Closed! Cannot afford {new_list[0]}.")
            is_closed = True
            break

if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
