inp_string = input()

capitals_index_list = []

for i in range(len(inp_string)):
    if 65 <= ord(inp_string[i]) <= 90:
        capitals_index_list.append(i)

print(capitals_index_list)
