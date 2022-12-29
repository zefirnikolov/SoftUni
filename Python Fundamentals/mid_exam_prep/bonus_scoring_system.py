from math import ceil

number_of_students_eq_loops = int(input())
course_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_lectures = 0

for student in range(1, number_of_students_eq_loops + 1):
    attendances_for_a_student = int(input())

    if attendances_for_a_student > max_lectures:
        max_lectures = attendances_for_a_student

    total_bonus = attendances_for_a_student / course_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus

print(f'Max Bonus: {ceil(max_bonus)}.')
print(f"The student has attended {max_lectures} lectures.")
