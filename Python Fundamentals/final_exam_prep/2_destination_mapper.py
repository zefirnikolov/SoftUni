import re

search_pattern = r'(\=|\/)([A-Z][A-Za-z]{2,})\1'
text = input()
results = re.findall(search_pattern, text)
if results:
    destinations = [el[1] for el in results]
    print(f"Destinations: {', '.join(destinations)}")
    total_points = 0
    for element in destinations:
        total_points += len(element)
    print(f'Travel Points: {total_points}')
else:
    print(f'Destinations: ')
    print(f'Travel Points: 0')
