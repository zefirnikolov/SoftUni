import re

search_pattern = r'(\#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
text = input()
results = re.findall(search_pattern, text)
if results:
    total_calories = sum([int(el[3]) for el in results])
    days = int(total_calories // 2000)
    print(f"You have food to last you for: {days} days!")
    for element in results:
        print(f"Item: {element[1]}, Best before: {element[2]}, Nutrition: {element[3]}")
else:
    print('You have food to last you for: 0 days!')
