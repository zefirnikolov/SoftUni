number_of_loops = int(input())

total_brackets_sum = ""
is_at_all = False

for _ in range(number_of_loops):
    current_input = input()

    if current_input == "(":
        is_at_all = True
        total_brackets_sum += "("
    elif current_input == ")":
        is_at_all = True
        total_brackets_sum += ")"

    if total_brackets_sum == "()":
        total_brackets_sum = ""

if is_at_all:
    if not total_brackets_sum:
        print("BALANCED")
    else:
        print('UNBALANCED')
