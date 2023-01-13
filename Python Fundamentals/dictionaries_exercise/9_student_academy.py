academy = {}
number_of_loops = int(input())

for _ in range(number_of_loops):
    student = input()
    grade = float(input())

    if not student in academy:
        academy[student] = []
    academy[student].append(grade)


average_grades = {}

for key, value in academy.items():
    grade_average = sum(value) / len(value)
    average_grades[key] = grade_average


bad_grades = [key for key, value in average_grades.items() if value < 4.50]
for element in bad_grades:
    if element in average_grades:
        del average_grades[element]

for student, student_grade in average_grades.items():
    print(f'{student} -> {student_grade:.2f}')
