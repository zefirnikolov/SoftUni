total_price_without_tax_or_discount = 0

while True:
    order = input()
    last_action = order

    if order == "special" or order == "regular":
        break

    if float(order) < 0:
        print("Invalid price!")
        continue

    total_price_without_tax_or_discount += float(order)

if total_price_without_tax_or_discount == 0:
    print("Invalid order!")

taxes = total_price_without_tax_or_discount * 0.2

total_price = total_price_without_tax_or_discount + taxes
if last_action == "special":
    total_price *= 0.9

if not total_price_without_tax_or_discount == 0:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price_without_tax_or_discount:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n-----------\nTotal price: {total_price:.2f}$")
