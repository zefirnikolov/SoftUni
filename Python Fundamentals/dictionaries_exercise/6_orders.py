orders = {}
while True:
    command = input()
    if command == "buy":
        break

    action_list = command.split()
    product_name = action_list[0]
    price = float(action_list[1])
    quantity = int(action_list[2])

    if not product_name in orders:
        orders[product_name] = {'price': price, 'quantity': quantity}
    else:
        if orders[product_name]['price'] == price:
            orders[product_name]['quantity'] += quantity
        else:
            orders[product_name]['price'] = price
            orders[product_name]['quantity'] += quantity

for key, value in orders.items():
    total_price = orders[key]['price'] * orders[key]['quantity']
    print(f"{key} -> {total_price:.2f}")
