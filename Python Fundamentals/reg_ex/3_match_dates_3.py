import re

search_pattern = r'(\d{2})(\.|\-|\/)([A-Z][a-z]{2})\2(\d{4})'
text = input()

results = re.findall(search_pattern, text)

for element in results:
    print(f'Day: {element[0]}, Month: {element[2]}, Year: {element[3]}')
