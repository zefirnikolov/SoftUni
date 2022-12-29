# tail = input()
# body = input()
# head = input()
#
# zoo_list = [head, body, tail]
#
# print(zoo_list)

zoo_list = []

for _ in range(3):
    current_string = input()
    zoo_list.append(current_string)

print(zoo_list[::-1])
