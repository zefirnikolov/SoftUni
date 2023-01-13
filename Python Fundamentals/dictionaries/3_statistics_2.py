products = {}

while True:
    command = input()
    if command == 'statistics':
        break
    new_list = command.split(": ")
    element = new_list[0]
    quantity = int(new_list[1])
    if not element in products:
        products[element] = quantity
    else:
        products[element] += quantity

print("Products in stock:")
for element, quantity in products.items():
    print(f'- {element}: {quantity}')
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
