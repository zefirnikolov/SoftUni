number_of_jury = int(input())
presentation = input()
sum_of_all_grades = 0
counter = 0

while presentation != 'Finish':
    sum_current_grades = 0

    for _ in range(number_of_jury):
        current_grade = float(input())
        sum_current_grades += current_grade
        sum_of_all_grades += current_grade
        counter += 1

    print(f"{presentation} - {(sum_current_grades / number_of_jury):.2f}.")

    presentation = input()

print(f"Student's final assessment is {(sum_of_all_grades / counter):.2f}.")
