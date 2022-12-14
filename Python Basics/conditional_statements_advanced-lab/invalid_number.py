number = int(input())

the_right_numbers = 100 <= number <= 200 or number == 0
if not the_right_numbers:
    print("invalid")
