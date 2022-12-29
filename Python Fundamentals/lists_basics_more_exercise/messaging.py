char_list = list(map(str, input().split()))
message_to_check = input()

message = []

for index in range(len(char_list)):
    element = char_list[index]
    index_find = 0
    for ele in element:
        index_find += int(ele)

    # if index_find > len(message_to_check):
    #     index_find = index_find - len(message_to_check)
    index_find %= len(message_to_check)
    message.append(message_to_check[index_find])
    # message_to_check = message_to_check[0:index_find:] + message_to_check[index_find + 1::]
    message_to_check = message_to_check.replace(message_to_check[index_find], '', 1)

print(''.join([x for x in message]))
