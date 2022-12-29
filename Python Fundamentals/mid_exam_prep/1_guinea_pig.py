food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
pig_weight = float(input()) * 1000

is_food_not_enough = False

for day_eq_element in range(1, 31):
    food -= 300
    if food <= 0:
        is_food_not_enough = True
        break
    if day_eq_element % 2 == 0:
        hay -= (food * 0.05)
        if hay <= 0:
            is_food_not_enough = True
            break
    if day_eq_element % 3 == 0:
        cover -= (pig_weight * 1 / 3)
        if cover <= 0:
            is_food_not_enough = True
            break

if is_food_not_enough:
    print("Merry must go to the pet store!")
else:
    print(
        f"Everything is fine! "
        f"Puppy is happy! Food: {(food / 1000):.2f}, Hay: {(hay / 1000):.2f}, Cover: {(cover / 1000):.2f}.")
