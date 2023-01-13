number_of_loops = int(input())
champions = {}

for _ in range(number_of_loops):
    hero_name, hp, mp = input().split(" ")
    champions[hero_name] = [int(hp), int(mp)]

while True:
    command = input()
    if command == 'End':
        break
    action_list = command.split(" - ")
    current_action = action_list[0]
    hero_name = action_list[1]
    if current_action == 'CastSpell':
        need_mp = int(action_list[2])
        spell_name = action_list[3]
        if champions[hero_name][1] >= need_mp:
            champions[hero_name][1] -= need_mp
            print(f"{hero_name} has successfully cast {spell_name} and now has {champions[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif current_action == 'TakeDamage':
        damage = int(action_list[2])
        attacker = action_list[3]
        champions[hero_name][0] -= damage
        if champions[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {champions[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del champions[hero_name]
    elif current_action == 'Recharge':
        amount = int(action_list[2])
        champions[hero_name][1] += amount
        if champions[hero_name][1] > 200:
            difference = champions[hero_name][1] - 200
            refill = amount - difference
            champions[hero_name][1] = 200
            print(f"{hero_name} recharged for {refill} MP!")
        else:
            print(f"{hero_name} recharged for {amount} MP!")
    elif current_action == "Heal":
        amount = int(action_list[2])
        champions[hero_name][0] += amount
        if champions[hero_name][0] > 100:
            difference = champions[hero_name][0] - 100
            refill = amount - difference
            champions[hero_name][0] = 100
            print(f"{hero_name} healed for {refill} HP!")
        else:
            print(f"{hero_name} healed for {amount} HP!")
for key, value in champions.items():
    print(key)
    print(f'  HP: {value[0]}')
    print(f'  MP: {value[1]}')
