from sys import maxsize

number_before_stop = input()
max_number = -maxsize

while number_before_stop != "Stop":
    parse_int_from_number = int(number_before_stop)

    if parse_int_from_number > max_number:
        max_number = parse_int_from_number

    number_before_stop = input()

print(max_number)
