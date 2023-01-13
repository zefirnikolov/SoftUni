first_string, second_string = input().split()

total_sum = 0

if len(first_string) > len(second_string):
    remaining_elements = len(first_string) - len(second_string)
    second_string += chr(1) * remaining_elements

if len(second_string) > len(first_string):
    remaining_elements = len(second_string) - len(first_string)
    first_string += chr(1) * remaining_elements

for index in range(len(first_string)):
    total_sum += ord(first_string[index]) * ord(second_string[index])

print(total_sum)
