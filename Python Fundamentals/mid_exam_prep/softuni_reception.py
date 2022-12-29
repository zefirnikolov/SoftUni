first_receptionist = int(input())
second_receptionist = int(input())
third_receptionist = int(input())
students = int(input())

students_for_hour = first_receptionist + second_receptionist + third_receptionist
hours = 0

while students > 0:
    students -= students_for_hour
    hours += 1
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")
