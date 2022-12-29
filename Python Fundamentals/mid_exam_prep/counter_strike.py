energy = int(input())

count = 0
is_energy = True

while True:
    command = input()

    if command == "End of battle":
        break

    distance_eq_energy_drain = int(command)

    if energy - distance_eq_energy_drain < 0:
        is_energy = False
        break

    energy -= distance_eq_energy_drain
    count += 1

    if count % 3 == 0:
        energy += count

if is_energy:
    print(f"Won battles: {count}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
