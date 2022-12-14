age_eq_number_of_loops = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toy_counter = 0
money = 0

for i_eq_current_birthday in range(1, age_eq_number_of_loops + 1):

    if i_eq_current_birthday % 2 == 1:
        toy_counter += 1
    else:
        money_increase = 10 * i_eq_current_birthday / 2  # i / 2 because you receive increase only in even cases.
        money += money_increase
        money -= 1

total_sum = money + toy_price * toy_counter
difference = abs(total_sum - washing_machine_price)

if total_sum >= washing_machine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
