miner_dict = {}
commodity: ''
quantity: ''
counter = 0
while True:
    command = input()
    if command == 'stop':
        break

    if counter % 2 == 0:
        commodity = command
    else:
        quantity = int(command)
        if commodity not in miner_dict:
            miner_dict[commodity] = quantity
        else:
            miner_dict[commodity] += quantity

    counter += 1

for key, value in miner_dict.items():
    print(f"{key} -> {value}")
