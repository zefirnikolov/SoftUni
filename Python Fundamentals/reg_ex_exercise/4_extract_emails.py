import re

text = input()
search_pattern = r'(^|(?<=\s))[A-Za-z0-9][A-Za-z0-9\-_.]+[a-zA-Z0-9]@[a-zA-Z][a-zA-Z\-]+[a-zA-Z]\.[a-zA-Z][a-zA-Z\-.]+\b'
# Not perfect search patter - It might be 0 chars after the 1st, which means I should use * instead if +
matches = re.finditer(search_pattern, text)
for match in matches:
    print(match.group())
