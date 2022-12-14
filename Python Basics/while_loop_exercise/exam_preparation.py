number_of_bad_grades = int(input())
problem_name = input()

bad_grades_counter = 0
total_sum_grade = 0
counter = 0
last_problem = ""
is_too_much_bad_grades = False

while problem_name != "Enough":
    grade = int(input())

    if grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == number_of_bad_grades:
            is_too_much_bad_grades = True
            break

    total_sum_grade += grade
    counter += 1
    last_problem = problem_name
    problem_name = input()

if is_too_much_bad_grades:
    print(f"You need a break, {bad_grades_counter} poor grades.")
else:
    print(f"Average score: {(total_sum_grade / counter):.2f}")
    print(f"Number of problems: {counter}")
    print(f"Last problem: {last_problem}")
