import re

search_pattern = r'(^|(?<=\s))([A-Za-z0-9][A-Za-z0-9\.\-\_]*[A-Za-z0-9])@' \
                 r'([A-Za-z][A-Za-z\-]*[A-Za-z])(\.[A-Za-z][A-Za-z\-]*[A-Za-z])+'
text = input()
results = re.finditer(search_pattern, text)
for match in results:
    print(match.group())
