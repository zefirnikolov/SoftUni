persons_to_elevate = int(input())
elevator_capacity = int(input())
add_course = 0

if persons_to_elevate <= elevator_capacity:
    add_course += 1

elif persons_to_elevate % elevator_capacity != 0:
    add_course += 1

courses = int(persons_to_elevate / elevator_capacity) + add_course

print(courses)
