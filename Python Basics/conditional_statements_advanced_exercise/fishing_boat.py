budget = int(input())
season = input()
number_of_fishermen = int(input())

price_for_rent = 0

if season == "Spring":
    price_for_rent = 3000

elif season == 'Summer' or season == 'Autumn':
    price_for_rent = 4200

elif season == 'Winter':
    price_for_rent = 2600

if number_of_fishermen <= 6:
    price_for_rent *= 0.9

elif 7 < number_of_fishermen <= 11:
    price_for_rent *= 0.85

elif number_of_fishermen > 11:
    price_for_rent *= 0.75

if (season != "Autumn") and (number_of_fishermen % 2 == 0):
    price_for_rent *= 0.95

difference = abs(price_for_rent - budget)

if budget >= price_for_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
