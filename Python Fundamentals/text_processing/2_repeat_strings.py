def repeater(data):
    new_text = data * len(data)
    return new_text


results = ''
new_list = input().split()

for element in new_list:
    repeated_element = repeater(element)
    results += repeated_element

print(results)
