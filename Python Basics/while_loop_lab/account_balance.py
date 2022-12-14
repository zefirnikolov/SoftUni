numbers_till_NoMoreMoney = input()
total_sum = 0

while numbers_till_NoMoreMoney != "NoMoreMoney":
    parse_to_float_numbers = float(numbers_till_NoMoreMoney)

    if parse_to_float_numbers < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {parse_to_float_numbers:.2f}")
    total_sum += parse_to_float_numbers
    numbers_till_NoMoreMoney = input()

print(f"Total: {total_sum:.2f}")
