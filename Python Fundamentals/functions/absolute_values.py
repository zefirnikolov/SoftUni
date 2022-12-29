new_list = input().split()
abs_list = []

for element in new_list:
    abs_list.append(abs(float(element)))

print(abs_list)
 