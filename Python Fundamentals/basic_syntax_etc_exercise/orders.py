number_of_order_eq_loops = int(input())

total_price = 0

for _ in range(number_of_order_eq_loops):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_needed <= 2000:
        current_price = price_per_capsule * days * capsules_needed
        print(f"The price for the coffee is: ${current_price:.2f}")
        total_price += current_price
    else:
        continue

    # if not 0.01 <= price_per_capsule <= 100:
    #     continue
    #
    # if not 1 <= days <= 31:
    #     continue
    #
    # if not 1 <= capsules_needed <= 2000:
    #     continue

    # current_price = price_per_capsule * days * capsules_needed
    # print(f"The price for the coffee is: ${current_price:.2f}")
    # total_price += current_price

print(f"Total: ${total_price:.2f}")
