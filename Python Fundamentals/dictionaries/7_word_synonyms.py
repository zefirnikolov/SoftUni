number_of_words = int(input())
synonyms_dict = {}
key = ''
value = ''
for i in range(number_of_words * 2):
    word = input()
    if i % 2 == 0:
        key = word
    else:
        value = word
        if not key in synonyms_dict:
            synonyms_dict[key] = value
        else:
            synonyms_dict[key] += f", {value}"

for key, value in synonyms_dict.items():
    print(f"{key} - {value}")
