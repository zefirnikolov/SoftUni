action_list = list(map(int, input().split(", ")))
minimum_wealth = int(input())

for index in range(len(action_list)):
    max_index = action_list.index(max(action_list))
    element = action_list[index]
    if index == max_index:
        continue
    else:
        if element < minimum_wealth:
            difference = minimum_wealth - element
            action_list[index] += difference
            action_list[max_index] -= difference

fail_counter = 0
for element in action_list:
    if element < minimum_wealth:
        fail_counter += 1

if fail_counter > 0:
    print('No equal distribution possible')
else:
    print(action_list)
