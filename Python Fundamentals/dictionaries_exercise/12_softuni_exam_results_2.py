results = {}
submissions = {}

while True:
    command = input()
    if command == 'exam finished':
        break
    action_list = command.split("-")
    student_name = action_list[0]
    if len(action_list) == 3:
        course = action_list[1]
        points = int(action_list[2])
        if not student_name in results:
            results[student_name] = 0
        if points > results[student_name]:
            results[student_name] = points
        if not course in submissions:
            submissions[course] = 0
        submissions[course] += 1
    if len(action_list) == 2:
        del results[student_name]

print("Results:")
for key, value in results.items():
    print(f'{key} | {value}')
print('Submissions:')
for key, value in submissions.items():
    print(f'{key} - {value}')
