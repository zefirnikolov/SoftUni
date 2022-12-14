movie_name = input()

student_counter = 0
standard_counter = 0
kid_counter = 0
total_tickets_counter = 0

while movie_name != "Finish":
    free_sits = int(input())
    type_of_ticket = input()

    counter_for_sits = 0

    while type_of_ticket != "End":
        counter_for_sits += 1
        if type_of_ticket == 'student':
            student_counter += 1
        elif type_of_ticket == 'standard':
            standard_counter += 1
        elif type_of_ticket == 'kid':
            kid_counter += 1

        total_tickets_counter += 1
        if counter_for_sits == free_sits:
            break

        type_of_ticket = input()

    print(f"{movie_name} - {(counter_for_sits / free_sits * 100):.2f}% full.")

    movie_name = input()

print(f"Total tickets: {total_tickets_counter}")
print(f"{(student_counter / total_tickets_counter * 100):.2f}% student tickets.")
print(f"{(standard_counter / total_tickets_counter * 100):.2f}% standard tickets.")
print(f"{(kid_counter / total_tickets_counter * 100):.2f}% kids tickets.")
