text = input().lower().split()
odd_occurrences = {}

for index in range(len(text)):
    element = text[index]

    if element not in odd_occurrences:
        odd_occurrences[element] = 0
    odd_occurrences[element] += 1

for key, value in odd_occurrences.items():
    if value % 2 == 1:
        print(key, end=' ')
