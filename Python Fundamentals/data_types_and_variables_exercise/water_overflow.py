number_of_pours_eq_loops = int(input())

capacity = 255
added_liters = 0

for _ in range(number_of_pours_eq_loops):
    current_add = int(input())

    if current_add + added_liters > capacity:
        print(f'Insufficient capacity!')
        continue

    added_liters += current_add

print(added_liters)
