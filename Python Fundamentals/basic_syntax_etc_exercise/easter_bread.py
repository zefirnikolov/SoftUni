budget = float(input())
price_for_1_kg_flour = float(input())

price_for_eggs = price_for_1_kg_flour * 0.75
price_for_1_l_milk = price_for_1_kg_flour * 0.25 + price_for_1_kg_flour
price_for_250_ml_milk = price_for_1_l_milk / 4

one_loaf_price = price_for_250_ml_milk + price_for_eggs + price_for_1_kg_flour

bread_counter = 0

loaves_made = int(budget / one_loaf_price)
money_left = budget - loaves_made * one_loaf_price

colored_eggs_counter = 0

for current_bread in range(1, loaves_made + 1):
    bread_counter += 1
    colored_eggs_counter += 3
    if current_bread % 3 == 0:
        colored_eggs_counter -= bread_counter - 2

print(f"You made {loaves_made} loaves of Easter bread! Now you have {colored_eggs_counter} eggs"
      f" and {money_left:.2f}BGN left.")
