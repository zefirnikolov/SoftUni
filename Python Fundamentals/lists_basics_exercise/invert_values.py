values = input()  # str_list = input().split()

str_list = values.split()  # == values.split(" ")
int_list = []

for element in str_list:
    int_list.append(-int(element))

print(int_list)
