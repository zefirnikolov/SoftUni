import re

search_pattern = r'>>([A-Za-z]+)<<(\d+)(\.\d+)?!(\d+)'
total_sum = 0
items = []
while True:
    text = input()
    if text == "Purchase":
        break
    result = re.findall(search_pattern, text)
    if result:
        items.append(result[0])

print('Bought furniture:')
for element in items:
    print(element[0])
    total_sum += float(element[1]+element[2]) * int(element[3])
print(f'Total money spend: {total_sum:.2f}')
