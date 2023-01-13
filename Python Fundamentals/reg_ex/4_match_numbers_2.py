import re

search_pattern = r'(^|(?<=\s))([0]|-?[1-9][0-9]*)(\.\d+)?($|(?=\s))'
text = input()

results = re.finditer(search_pattern, text)
for match in results:
    print(match.group(), end=" ")
