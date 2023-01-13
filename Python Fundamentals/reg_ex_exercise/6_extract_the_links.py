import re

search_pattern = r'(www\.)([a-zA-Z0-9-]+)\.([a-z]+)([.a-z*])+'

while True:
    text = input()
    if not text:
        break

    matches = re.finditer(search_pattern, text)
    for element in matches:
        print(element.group())
