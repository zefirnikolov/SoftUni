import re

names = input()
search_pattern = r"\b[A-Z][a-z]+\ [A-Z][a-z]+\b"
matches = re.findall(search_pattern, names, re.UNICODE)
print(' '.join(matches))
