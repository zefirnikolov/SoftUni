import re

search_pattern = r'(\:.)'
text = input()

result = re.findall(search_pattern, text)
for element in result:
    print(result)
