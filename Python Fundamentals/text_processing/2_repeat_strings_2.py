new_list = input().split()
last_list = []

for element in new_list:
    last_list.append(element * len(element))

print(''.join(last_list))
