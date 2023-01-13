softuni_courses = {}

while True:
    command = input()
    if command == 'end':
        break

    action_list = command.split(" : ")
    course_name = action_list[0]
    student_name = action_list[1]

    if not course_name in softuni_courses:
        softuni_courses[course_name] = []
    softuni_courses[course_name].append(student_name)

for key, value in softuni_courses.items():
    print(f'{key}: {len(value)}')
    for element in value:
        print(f'-- {element}')
