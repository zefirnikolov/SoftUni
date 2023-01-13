import re

text = input()
search_pattern = r'(^|(?<=\s))[A-Za-z0-9][A-Za-z0-9-_.]*@[a-zA-Z][a-zA-Z-]*\.[a-zA-Z][a-zA-Z\-.]*\b'
matches = re.finditer(search_pattern, text)
for match in matches:
    print(match.group())
# All patterns must be in groups to use findall
# matches = re.findall(search_pattern, text)
# print(matches)
