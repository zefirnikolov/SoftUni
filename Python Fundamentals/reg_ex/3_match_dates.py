import re

dates = input()
search_pattern = r'\b\d{2}\/[A-Z][a-z]{2}\/\d{4}\b|\b\d{2}\-[A-Z][a-z]{2}\-\d{4}\b|\b\d{2}\.[A-Z][a-z]{2}\.\d{4}\b'
matches = re.findall(search_pattern, dates)
day = []
month = []
year = []
for element in matches:
    day.append(element[0] + element[1])
    month.append(element[3:6])
    year.append(element[7:len(element):])

for index in range(len(day)):
    print(f"Day: {day[index]}, Month: {month[index]}, Year: {year[index]}")
