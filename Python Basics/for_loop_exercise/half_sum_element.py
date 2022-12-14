from sys import maxsize

number_of_loops = int(input())
max_number = -maxsize
total_sum = 0

for _ in range(number_of_loops):
    current_number = int(input())
    total_sum += current_number

    if current_number > max_number:
        max_number = current_number

difference = abs(total_sum - max_number - max_number)

if total_sum - max_number == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f'Diff = {difference}')
