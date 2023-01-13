import re

dates = input()
search_pattern = r"\b(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})\b"
matches = re.findall(search_pattern, dates)

for element in matches:
    print(f"Day: {element[0]}, Month: {element[2]}, Year: {element[3]}")
