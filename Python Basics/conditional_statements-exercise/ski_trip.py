number_of_days = int(input())
type_of_room = input()
evaluation = input()

night_stays = number_of_days - 1
price_per_night = 0

if type_of_room == "room for one person":
    price_per_night = 18

elif type_of_room == "apartment":
    price_per_night = 25
    if number_of_days < 10:
        price_per_night *= 0.7
    elif number_of_days <= 15:
        price_per_night *= 0.65
    else:
        price_per_night *= 0.5

elif type_of_room == "president apartment":
    price_per_night = 35
    if number_of_days < 10:
        price_per_night *= 0.9
    elif number_of_days <= 15:
        price_per_night *= 0.85
    else:
        price_per_night *= 0.8

all_sum = price_per_night * night_stays

if evaluation == 'positive':
    all_sum *= 1.25

else:
    all_sum *= 0.9

print(f"{all_sum:.2f}")
