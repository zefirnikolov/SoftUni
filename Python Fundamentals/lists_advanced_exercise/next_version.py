version_list = [int(element) for element in input().split(".")]

if version_list[2] < 10:
    if version_list[2] == 9 and version_list[1] != 9:
        version_list[2] = 0
        version_list[1] += 1
    elif version_list[2] < 9:
        version_list[2] += 1
    else:
        version_list[0] += 1
        version_list[1] = 0
        version_list[2] = 0

version_string = '.'.join(map(str, version_list))
print(version_string)
