import re

search_pattern = r'\b(\_)([A-Za-z0-9]+)\b'
text = input()

results = re.findall(search_pattern, text)
items = []
for index in range(len(results)):
    items.append(results[index][1])
print(','.join(items))
