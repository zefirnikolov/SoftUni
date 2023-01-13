junk_dict = {}
inventory_dict = {}
item = ''
digit = 0
is_created = False
is_found = False

while True:
    if is_found:
        break
    random_items = [item.lower() for item in input().split()]
    for index, element in enumerate(random_items):
        if index % 2 == 0:
            digit = int(element)
        else:
            item = element
            if item == "shards" or item == "fragments" or item == "motes":
                if not is_created:
                    inventory_dict["shards"] = 0
                    inventory_dict['fragments'] = 0
                    inventory_dict['motes'] = 0
                    is_created = True
                inventory_dict[item] += digit
                if inventory_dict[item] >= 250:
                    inventory_dict[item] -= 250
                    is_found = True
                    break
            else:
                if item not in junk_dict:
                    junk_dict[item] = 0
                junk_dict[item] += digit

if item == "shards":
    item = "Shadowmourne"
elif item == 'fragments':
    item = 'Valanyr'
elif item == 'motes':
    item = 'Dragonwrath'

print(f"{item} obtained!")
for item_key, number in inventory_dict.items():
    print(f'{item_key}: {number}')
for item_key, number in junk_dict.items():
    print(f'{item_key}: {number}')
