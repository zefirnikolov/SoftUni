results = {}
submissions = {}
# Possible pitfall - if one user has more than 1 language
while True:
    command = input()
    if command == 'exam finished':
        break

    action_list = command.split("-")
    if len(action_list) == 3:
        username = action_list[0]
        language = action_list[1]
        points = int(action_list[2])   # If there is obvious points - you must always make that int!

        if username not in results:
            results[username] = {language: points}
        else:
            for key, value in results.items():

                for key_2, value_2 in value.items():
                    if username == key:
                        if points > value_2:
                            results[username][language] = points
                            break

        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
    else:
        username = action_list[0]
        banning = action_list[1]
        if banning == 'banned':
            if username in results:
                del results[username]

print("Results:")
for user, contest in results.items():
    for points in contest.values():
        print(f'{user} | {points}')

print("Submissions:")
for language, count in submissions.items():
    print(f'{language} - {count}')
