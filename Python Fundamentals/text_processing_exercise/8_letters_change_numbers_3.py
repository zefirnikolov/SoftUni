new_list = input().split()
total_sum = 0

for index in range(len(new_list)):
    element = new_list[index]

    first_letter = element[0]
    last_letter = element[-1]
    number = int(element[1:len(element) - 1:])

    if first_letter.isupper():
        divide = 0
        for ind in range(ord('A'), ord('Z') + 1):
            if first_letter == chr(ind):
                divide = ind - 64
        total_sum += number / divide
    elif first_letter.islower():
        multiply = 0
        for ind_2 in range(ord('a'), ord('z') + 1):
            if first_letter == chr(ind_2):
                multiply = ind_2 - 96
        total_sum += number * multiply

    if last_letter.isupper():
        subtract = 0
        for ind_3 in range(ord('A'), ord('Z') + 1):
            if last_letter == chr(ind_3):
                subtract = ind_3 - 64
        total_sum -= subtract
    elif last_letter.islower():
        add = 0
        for ind_4 in range(ord('a'), ord('z') + 1):
            if last_letter == chr(ind_4):
                add = ind_4 - 96
        total_sum += add

print(f'{total_sum:.2f}')
