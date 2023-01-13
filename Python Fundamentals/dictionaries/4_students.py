students = {}

while True:
    command = input()
    if not ":" in command:
        break
    action_list = command.split(":")
    key = int(action_list[1])
    nested_dict = {'name': action_list[0], 'course': action_list[2]}
    students[key] = nested_dict

command = command.replace('_', ' ')

for key, value in students.items():
    for nested_key, nested_value in value.items():
        if command == nested_value:
            print(f"{students[key]['name']} - {key}")
