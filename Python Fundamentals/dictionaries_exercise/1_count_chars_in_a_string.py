data = input()
chars_dict = {}

for ele in data:
    if ele == " ":
        continue
    if not ele in chars_dict:
        chars_dict[ele] = 0
    chars_dict[ele] += 1

print(chars_dict)
for key, value in chars_dict.items():
    print(f"{key} -> {value}")
