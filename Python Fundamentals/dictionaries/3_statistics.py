stock_dict = {}
while True:
    command = input()
    if command == 'statistics':
        break
    action_list = command.split(": ")
    product_eq_key = action_list[0]
    quantity_eq_value = int(action_list[1])
    if product_eq_key not in stock_dict:
        stock_dict[product_eq_key] = quantity_eq_value
    else:
        stock_dict[product_eq_key] += quantity_eq_value


print("Products in stock:")
for product_eq_key, quantity_eq_value in stock_dict.items():
    print(f'- {product_eq_key}: {quantity_eq_value}')
print(f"Total Products: {len(stock_dict)}")
print(f"Total Quantity: {sum(stock_dict.values())}")
