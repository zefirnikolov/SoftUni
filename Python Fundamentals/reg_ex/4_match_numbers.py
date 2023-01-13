import re

text = input()
search_pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'  # it can, or it can't have - upfront - -?
matches = re.finditer(search_pattern, text)
# for element in matches:
#     print(element[1], end=" ")
for match in matches:
    print(match.group(), end=" ")
