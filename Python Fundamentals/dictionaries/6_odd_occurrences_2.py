data = [element.lower() for element in input().split()]
new_dict = {}

for element in data:
    if not element in new_dict:
        new_dict[element] = 0
    new_dict[element] += 1

result = []
for key, value in new_dict.items():
    if value % 2 == 1:
        result.append(key)

print(' '.join(result))
