number_until_stop = input()

sum_prime_numbers = 0
sum_non_prime_numbers = 0

while number_until_stop != "stop":
    int_number = int(number_until_stop)
    if int_number < 0:
        print("Number is negative.")
        int_number = 0

    for i in range(2, int_number):  # for loop is checking is the number prime or not!
        if int_number == 0 or int_number == 1:
            sum_non_prime_numbers += int_number
            break

        if int_number % i == 0:
            sum_non_prime_numbers += int_number
            break

    else:
        sum_prime_numbers += int_number

    number_until_stop = input()

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")
