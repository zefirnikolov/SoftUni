import re

search_pattern = r'\+359(\s|\-)2\1\d{3}\1\d{4}\b'
text = input()

results = re.finditer(search_pattern, text)
matches = []
for match in results:
    matches.append(match.group())
print(", ".join(matches))
