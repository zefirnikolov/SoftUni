def man_o_war_func(pirate_ship: list, war_ship: list):
    maximum_health_for_section = int(input())

    is_retire = False
    is_pirate_ship_sunk = False
    is_war_ship_sunk = False

    while True:
        command = input()

        if command == 'Retire':
            is_retire = True
            break

        action_list = command.split()
        current_action = action_list[0]

        if current_action == "Fire":
            index = int(action_list[1])
            if index in range(len(war_ship)):
                damage = int(action_list[2])
                war_ship[index] -= damage
                if war_ship[index] <= 0:
                    print(f"You won! The enemy ship has sunken.")
                    is_war_ship_sunk = True
                    break
            if is_war_ship_sunk:
                break

        elif current_action == "Defend":
            start_index = int(action_list[1])
            end_index = int(action_list[2])
            damage = int(action_list[3])
            if start_index in range(len(pirate_ship)) and end_index in range(len(pirate_ship)):
                for index in range(len(pirate_ship)):
                    if start_index <= index <= end_index:
                        pirate_ship[index] -= damage
                        if pirate_ship[index] <= 0:
                            print("You lost! The pirate ship has sunken.")
                            is_pirate_ship_sunk = True
                            break
            if is_pirate_ship_sunk:
                break

        elif current_action == "Repair":
            index = int(action_list[1])
            health = int(action_list[2])
            if index in range(len(pirate_ship)):
                pirate_ship[index] += health
                if pirate_ship[index] > maximum_health_for_section:
                    pirate_ship[index] = maximum_health_for_section

        elif current_action == "Status":
            status_counter = 0
            for element in pirate_ship:
                if element < maximum_health_for_section * 0.2:
                    status_counter += 1
            print(f"{status_counter} sections need repair.")

    if is_retire:
        print(f"Pirate ship status: {sum(pirate_ship)}")
        print(f"Warship status: {sum(war_ship)}")


pirate_list = list(map(int, input().split(">")))
war_ship_list = list(map(int, input().split(">")))
man_o_war_func(pirate_list, war_ship_list)
