number_of_loops = int(input())

synonyms = {}
for _ in range(number_of_loops):
    word = input()
    similar = input()

    if not word in synonyms:
        synonyms[word] = []
    synonyms[word].append(similar)

for key, value in synonyms.items():
    all_synonyms = ", ".join(value)
    print(f"{key} - {all_synonyms}")
