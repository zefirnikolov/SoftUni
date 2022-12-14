from sys import maxsize

easter_breads_number = int(input())

max_points = -maxsize
best_baker = ''

for _ in range(easter_breads_number):
    baker_name = input()
    bread_grade = input()

    points_per_baker = 0

    while bread_grade != "Stop":
        bread_grade_to_int = int(bread_grade)

        points_per_baker += bread_grade_to_int

        bread_grade = input()

    print(f"{baker_name} has {points_per_baker} points.")

    if points_per_baker > max_points:
        print(f"{baker_name} is the new number 1!")
        best_baker = baker_name
        max_points = points_per_baker

print(f"{best_baker} won competition with {max_points} points!")
