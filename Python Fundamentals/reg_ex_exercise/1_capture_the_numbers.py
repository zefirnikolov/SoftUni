import re

regex = r"\d+"
line = input()
new_text = []
while True:

    if line:
        matches = re.findall(regex, line)
        if matches:
            print(' '.join(matches), end=" ")
        line = input()
    else:
        break
