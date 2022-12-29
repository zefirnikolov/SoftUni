number_of_elements_eq_loops = int(input())

matrix = []

for element in range(number_of_elements_eq_loops):
    small_list = list(map(int, input().split()))
    matrix.append(small_list)

actions_list = input().split()

lost_ships = 0

for element_2 in actions_list:
    row = int(element_2[0])
    column = int(element_2[2])
    if matrix[row][column] > 0:
        matrix[row][column] -= 1
        if matrix[row][column] == 0:
            lost_ships += 1
    else:
        continue

print(lost_ships)
