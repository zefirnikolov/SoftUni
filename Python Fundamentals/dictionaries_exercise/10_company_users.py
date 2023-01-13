users = {}

while True:
    command = input()

    if command == 'End':
        break

    action_list = command.split(" -> ")
    company_name = action_list[0]
    employee_id = action_list[1]

    if company_name not in users:
        users[company_name] = []
    if employee_id not in users[company_name]:
        users[company_name].append(employee_id)

for key, value in users.items():
    print(key)
    for element in value:
        print(f'-- {element}')
