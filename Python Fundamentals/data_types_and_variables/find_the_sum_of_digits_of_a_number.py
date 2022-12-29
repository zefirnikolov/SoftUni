current_number = int(input("Enter Number: "))

current_number_sum = 0

while current_number != 0:
    current_number_sum += current_number % 10
    current_number = int(current_number / 10)

print(current_number_sum)
