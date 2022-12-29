lost_fights_count_eq_loops = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

shield_brake_counter = 0
total_expenses = 0

for fight_lost in range(1, lost_fights_count_eq_loops + 1):

    if fight_lost % 2 == 0:
        total_expenses += helmet_price

    if fight_lost % 3 == 0:
        total_expenses += sword_price

    if fight_lost % 2 == 0 and fight_lost % 3 == 0:
        shield_brake_counter += 1
        total_expenses += shield_price
        if shield_brake_counter % 2 == 0 and shield_brake_counter != 0:
            total_expenses += armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
