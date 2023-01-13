academy = {}

number_of_loops = int(input())

for _ in range(number_of_loops):
    student = input()
    current_grade = float(input())

    if student not in academy:
        academy[student] = []
    academy[student].append(current_grade)

passed_students = {}
for current_student, grades in academy.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        passed_students[current_student] = average_grade

for key, value in passed_students.items():
    print(f'{key} -> {value:.2f}')
