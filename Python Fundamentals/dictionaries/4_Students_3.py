students = {}

while True:
    command = input()
    if not ':' in command:
        break
    new_list = command.split(":")
    name = new_list[0]
    id_number = new_list[1]
    course = new_list[2]
    if not course in students:
        students[course] = {}
    students[course][id_number] = name

searched_course = command.replace('_', ' ')

for key, value in students.items():
    if key == searched_course:
        for nested_key, nested_value in value.items():
            print(f'{nested_value} - {nested_key}')
