new_list = input().split()

if len(new_list[0]) > len(new_list[1]):
    difference = len(new_list[0]) - len(new_list[1])
    new_list[1] += chr(1) * difference
elif len(new_list[1]) > len(new_list[0]):
    difference = len(new_list[1]) - len(new_list[0])
    new_list[0] += chr(1) * difference

text_first = new_list[0]
text_second = new_list[1]
total_sum = 0
for index in range(len(text_second)):
    element_1 = text_first[index]
    element_2 = text_second[index]
    total_sum += ord(element_1) * ord(element_2)

print(total_sum)
