num = int(input())
current_num = int(input())
total_sum = current_num

while total_sum < num:
    current_num = int(input())
    total_sum += current_num

print(total_sum)
