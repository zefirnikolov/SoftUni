dog_food_bought_kg = int(input())
dog_food_eaten_grams = input()

food_eaten_sum = 0

while dog_food_eaten_grams != 'Adopted':
    grams_food_eaten_int = int(dog_food_eaten_grams)
    food_eaten_sum += grams_food_eaten_int

    dog_food_eaten_grams = input()

difference = abs(food_eaten_sum - dog_food_bought_kg * 1000)

if food_eaten_sum <= dog_food_bought_kg * 1000:
    print(f"Food is enough! Leftovers: {difference} grams.")

else:
    print(f"Food is not enough. You need {difference} grams more.")
