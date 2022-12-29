tasks_list = []


while True:
    command_list = input().split('-')

    if command_list[0] == "End":
        break

    priority = int(command_list[0])
    task = command_list[1]
    tasks_list.append((priority, task))

print(sorted(tasks_list))
sorted_tasks = [task_data[1] for task_data in sorted(tasks_list)]
print(sorted_tasks)
