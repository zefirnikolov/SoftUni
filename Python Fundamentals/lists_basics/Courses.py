number_of_loops = int(input())

courses = []

for _ in range(number_of_loops):
    current_course = input()
    courses.append(current_course)
    # courses += [current_course]

print(courses)
