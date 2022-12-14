budget = float(input())
season = input()

destination = ''
camp_or_hotel = ''
spent_money = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == "summer":
        camp_or_hotel = "Camp"
        spent_money = budget * 0.3
    else:
        camp_or_hotel = "Hotel"
        spent_money = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == "summer":
        camp_or_hotel = "Camp"
        spent_money = budget * 0.4
    else:
        camp_or_hotel = "Hotel"
        spent_money = budget * 0.8
else:
    destination = 'Europe'
    camp_or_hotel = "Hotel"
    spent_money = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{camp_or_hotel} - {spent_money:.2f}')
