orders = {}

while True:
    command = input()
    if command == "buy":
        break
    new_list = command.split()
    product_name = new_list[0]
    price = float(new_list[1])
    quantity = int(new_list[2])

    if product_name not in orders:
        orders[product_name] = [0.0, 0]
    orders[product_name][0] = price
    orders[product_name][1] += quantity

for key, value in orders.items():
    total_price = value[0] * value[1]
    print(f'{key} -> {total_price:.2f}')
