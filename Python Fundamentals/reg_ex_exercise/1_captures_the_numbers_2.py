import re

while True:
    command = input()
    if command == "":
        break

    search_pattern = r'\d+'
    matched = re.finditer(search_pattern, command)
    for match in matched:
        print(match.group(), end=" ")
