courses = {}

while True:
    command = input()
    if command == 'end':
        break
    action_list = command.split(" : ")
    name_of_the_course = action_list[0]
    student_name = action_list[1]

    if not name_of_the_course in courses:
        courses[name_of_the_course] = []
    courses[name_of_the_course].append(student_name)

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for element in value:
        print(f"-- {element}")
