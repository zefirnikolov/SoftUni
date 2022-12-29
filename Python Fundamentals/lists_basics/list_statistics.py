number_of_lines_eq_loops = int(input())

positive_list = []
negative_list = []

for _ in range(number_of_lines_eq_loops):
    current_number = int(input())

    if current_number < 0:
        negative_list.append(current_number)
    else:
        positive_list.append(current_number)

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")
