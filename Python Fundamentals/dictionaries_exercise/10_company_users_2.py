users_of_company = {}

while True:
    command = input()
    if command == "End":
        break
    action_list = command.split(' -> ')
    current_company = action_list[0]
    employee_id = action_list[1]

    if current_company not in users_of_company:
        users_of_company[current_company] = {}
    users_of_company[current_company][employee_id] = 'employee'

for key, value in users_of_company.items():
    print(key)
    for nested_key in value.keys():
        print(f'-- {nested_key}')
