num1 = int(input())
num2 = int(input())
magic_number = int(input())

counter = 0
is_found = False

for i in range(num1, num2 + 1):

    for j in range(num1, num2 + 1):
        total_sum = i + j
        counter += 1

        if total_sum == magic_number:
            print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
            is_found = True
            break

    if is_found:
        break

if not is_found:
    print(f"{counter} combinations - neither equals {magic_number}")
