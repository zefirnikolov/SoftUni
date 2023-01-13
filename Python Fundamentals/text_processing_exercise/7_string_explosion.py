action_list = [letter for letter in input()]
new_list = []
counter = 0
for index in range(len(action_list)):
    element = action_list[index]

    if element == ">":
        counter += int(action_list[index + 1])
        new_list.append(element)
        continue
    if counter > 0:
        counter -= 1
        continue

    new_list.append(element)

print(''.join(new_list))
