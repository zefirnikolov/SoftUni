month = input()
number_of_stays = int(input())

studio_price_per_night = 0
apartment_price_per_night = 0

if month == "May" or month == "October":
    studio_price_per_night = 50
    apartment_price_per_night = 65
    if 7 < number_of_stays <= 14:
        studio_price_per_night *= 0.95
    elif number_of_stays > 14:
        studio_price_per_night *= 0.7

elif month == "June" or month == "September":
    studio_price_per_night = 75.2
    apartment_price_per_night = 68.7
    if number_of_stays > 14:
        studio_price_per_night *= 0.8

else:
    studio_price_per_night = 76
    apartment_price_per_night = 77

if number_of_stays > 14:
    apartment_price_per_night *= 0.9

final_price_for_apartment = apartment_price_per_night * number_of_stays
final_price_for_studio = studio_price_per_night * number_of_stays

print(f"Apartment: {final_price_for_apartment:.2f} lv.")
print(f"Studio: {final_price_for_studio:.2f} lv.")
