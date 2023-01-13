import re


text = input()
cool_threshold = 1

for element in text:
    if element.isdigit():
        cool_threshold *= int(element)

search_pattern = r'(::|\*\*)([A-Z][a-z]{2,})(\1)'
result = re.findall(search_pattern, text)

new_list = []

for element in result:
    sum_ele = 0
    for char in element[1]:
        sum_ele += ord(char)
    if sum_ele > cool_threshold:
        new_list.append(''.join(element))
print(f"Cool threshold: {cool_threshold}")
print(f'{len(result)} emojis found in the text. The cool ones are:')
for element in new_list:
    print(element)
