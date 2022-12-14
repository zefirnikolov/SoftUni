money_needed = float(input())
current_money = float(input())

total_sum = current_money
spend_counter = 0
all_days_counter = 0
is_broke = False

while total_sum < money_needed:
    type_of_action = input()
    spend_or_saved_money = float(input())
    all_days_counter += 1

    if type_of_action == "spend":
        total_sum -= spend_or_saved_money
        if total_sum < 0:
            total_sum = 0
        spend_counter += 1
        if spend_counter == 5:
            is_broke = True
            break

    else:
        total_sum += spend_or_saved_money
        spend_counter = 0

if is_broke:
    print("You can't save the money.")
    print(all_days_counter)

else:
    print(f"You saved the money for {all_days_counter} days.")
