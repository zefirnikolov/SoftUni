electrons = int(input())

filled_shells_list = []
shell_number = 0
while electrons > 0:
    shell_number += 1
    filled_electrons = 2 * (shell_number ** 2)
    if filled_electrons < electrons:
        filled_shells_list.append(filled_electrons)
    else:
        filled_shells_list.append(electrons)
    electrons -= 2 * (shell_number ** 2)

print(filled_shells_list)
