mined_resources = {}

while True:
    command = input()
    if command == 'stop':
        break
    value = int(input())

    if command not in mined_resources:
        mined_resources[command] = 0
    mined_resources[command] += value

for resource, quantity in mined_resources.items():
    print(f"{resource} -> {quantity}")
