import re

search_pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'
text = input()

results = re.finditer(search_pattern, text)
for match in results:
    print(match.group(), end=" ")

# results = re.findall(search_pattern, text)
# print(' '.join(results))
