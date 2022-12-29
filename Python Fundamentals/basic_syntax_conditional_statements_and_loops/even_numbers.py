number_of_loops = int(input())

is_odd = False
current_number = 0

for _ in range(number_of_loops):
    current_number = int(input())

    if current_number % 2 == 1:
        is_odd = True
        break

if is_odd:
    print(f"{current_number} is odd!")
else:
    print(f'All numbers are even.')
