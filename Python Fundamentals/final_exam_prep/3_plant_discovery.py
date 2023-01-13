discovered_plants = {}
rating = {}
number_of_loops = int(input())
for _ in range(number_of_loops):
    plant, rarity = input().split("<->")
    discovered_plants[plant] = int(rarity)

while True:
    command = input()
    if command == 'Exhibition':
        break
    action_list = command.split()
    current_action = action_list[0]
    plant = action_list[1]
    if plant not in discovered_plants:
        print('error')
        continue
    if current_action == "Rate:":
        if plant not in rating:
            rating[plant] = []
        rating[plant].append(int(action_list[3]))
    elif current_action == 'Update:':
        discovered_plants[plant] = int(action_list[3])
    elif current_action == 'Reset:':
        rating[plant].clear()

for element in discovered_plants:
    if element in rating:
        continue
    else:
        rating[element] = []

print('Plants for the exhibition:')
for key, value in discovered_plants.items():
    average_rating = 0
    if len(rating[key]) > 0:
        average_rating = sum(rating[key]) / len(rating[key])
    print(f'- {key}; Rarity: {value}; Rating: {average_rating:.2f}')
