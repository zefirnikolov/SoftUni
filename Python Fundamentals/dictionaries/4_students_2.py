students_dict = {}
command = input()
while ':' in command:

    name_eq_nested_value, student_id_eq_nested_key, course_eq_key = command.split(":")
    if course_eq_key not in students_dict:
        students_dict[course_eq_key] = {}
    students_dict[course_eq_key][student_id_eq_nested_key] = name_eq_nested_value
    command = input()

course_eq_key = ' '.join(command.split("_"))
for key, value in students_dict.items():
    if key == course_eq_key:
        for student_id_eq_nested_key, name_eq_nested_value in value.items():
            print(f"{name_eq_nested_value} - {student_id_eq_nested_key}")
