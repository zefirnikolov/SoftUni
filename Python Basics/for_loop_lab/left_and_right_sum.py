number_of_loops_in_the_beginning = int(input())

left_sum = 0
right_sum = 0

for i in range(1, number_of_loops_in_the_beginning * 2 + 1):
    current_number = int(input())
    if i / 2 < (number_of_loops_in_the_beginning + 1) / 2:
        left_sum += current_number
    else:
        right_sum += current_number

difference = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {difference}")
