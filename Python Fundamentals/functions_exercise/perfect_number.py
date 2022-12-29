def aliquot_compare(digit):
    aliquot_sum = 0
    for element in range(1, digit):
        if digit % element == 0:
            aliquot_sum += element
    if digit == aliquot_sum:
        return f"We have a perfect number!"
    return f"It's not so perfect."


number = int(input())
print(aliquot_compare(number))

# number = int(input())
#
# aliquot_sum = 0
# for i in range(1, number):
#     if number % i == 0:
#         aliquot_sum += i
#
# if number == aliquot_sum:
#     print("We have a perfect number!")
# else:
#     print("It's not so perfect.")
