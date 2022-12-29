names = input()

names_list = names.split(", ")
result = sorted(names_list, key=lambda item: (-len(item), item))
print(result)
