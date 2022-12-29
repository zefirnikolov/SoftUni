number = "123453635644"
name = "Gosho"

# enumerate in string - in number or name - strings

# for current_digit in range(len(number)):
#
#     if int(number[current_digit]) % 2 == 0:
#         print(number[current_digit])

for index, digit in enumerate(name):
    print(index, digit)

for index, digit in enumerate(number):
    print(index, digit)
