budget = float(input())
number_of_actors = int(input())
price_for_clothes_per_actor = float(input())

decor = budget * 0.1
if number_of_actors > 150:
    price_for_clothes_per_actor *= 0.9

sum_for_filming = decor + price_for_clothes_per_actor * number_of_actors

difference = abs(budget - sum_for_filming)
if sum_for_filming <= budget:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
