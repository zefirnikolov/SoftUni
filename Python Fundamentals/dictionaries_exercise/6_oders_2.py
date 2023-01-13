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
        orders[product_name] = {'price': 0.0, 'quantity': 0}
    orders[product_name]['price'] = price
    orders[product_name]['quantity'] += quantity


for key, value in orders.items():
    price = 0
    for nested_key, nested_value in value.items():
        product = key
        if nested_key == 'price':
            price = nested_value
        if nested_key == "quantity":
            print(f'{product} -> {(price * nested_value):.2f}')
