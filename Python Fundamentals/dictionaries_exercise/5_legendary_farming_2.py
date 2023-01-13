key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
is_found = False
legendary_item = ''
while True:
    text = [material.lower() for material in input().split()]
    for index in range(len(text)):
        element = text[index]
        if index % 2 == 1:
            if element == 'shards' or element == 'fragments' or element == 'motes':
                key_materials[element] += int(text[index - 1])
                if key_materials[element] >= 250:
                    key_materials[element] -= 250
                    is_found = True
                    if element == 'shards':
                        legendary_item = 'Shadowmourne'
                    elif element == 'fragments':
                        legendary_item = 'Valanyr'
                    elif element == 'motes':
                        legendary_item = 'Dragonwrath'
                    break
            else:
                if not element in junk:
                    junk[element] = 0
                junk[element] += int(text[index - 1])
    if is_found:
        break
print(f"{legendary_item} obtained!")
for key, value in key_materials.items():
    print(f"{key}: {value}")
for key, value in junk.items():
    print(f"{key}: {value}")
