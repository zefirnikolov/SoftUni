import re

text = input()
search_pattern = r'\b_([a-zA-Z\d]+)\b'

matches = re.findall(search_pattern,text)
print(','.join(matches))

