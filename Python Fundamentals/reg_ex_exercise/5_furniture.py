import re

search_pattern = r'^>{2}([a-zA-Z]+)<{2}([0]|[1-9][0-9]*)(\.\d+)?!([1-9][0-9]*)$'
furniture = []

while True:
    text = input()
    if text == 'Purchase':
        break

    matches = re.findall(search_pattern, text)
    if matches:
        furniture.append(matches[0])

if furniture:
    total_sum = 0
    for element in furniture:
        current_furniture = element[0]
        price = float(element[1] + element[2])
        if price == 0:
            continue
        quantity = int(element[3])
        if total_sum == 0:
            print("Bought furniture:")
        total_sum += price * quantity
        print(current_furniture)

    print(f"Total money spend: {total_sum:.2f}")
else:
    print("Bought furniture:")
    print('Total money spend: 0.00')
