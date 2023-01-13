number_of_days_eq_loops = int(input())
players = int(input())
energy = float(input())
water_per_day = float(input())
food_per_day = float(input())
is_not_finished = False

total_water = number_of_days_eq_loops * players * water_per_day
total_food = number_of_days_eq_loops * players * food_per_day


for day in range(1, number_of_days_eq_loops + 1):
    loss_energy = float(input())
    energy -= loss_energy
    if energy <= 0:
        is_not_finished = True
        break
    if day % 2 == 0:
        energy *= 1.05
        total_water *= 0.7
    if day % 3 == 0:
        total_food -= total_food / players
        energy *= 1.10

if is_not_finished:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
