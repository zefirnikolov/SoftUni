text = input()

occurrences = {}
for element in text:
    if element == " ":
        continue
    if not element in occurrences:
        occurrences[element] = 0
    occurrences[element] += 1

for key, value in occurrences.items():
    print(f"{key} -> {value}")
