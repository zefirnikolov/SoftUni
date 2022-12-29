version_list = [int(element) for element in input().split(".")]

version_list[-1] += 1

for current_index in range(len(version_list) - 1, -1, -1):
    if version_list[current_index] > 9:
        version_list[current_index] = 0
        if current_index -1 >= 0:
            version_list[current_index - 1] += 1

print('.'.join(str(x) for x in version_list))
