import re

text = input()
search_pattern = input()
regex = fr'\b{search_pattern}\b'
matches = re.findall(regex, text, re.IGNORECASE)
print(len(matches))
