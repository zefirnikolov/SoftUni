number_of_groups_eq_loops = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
sum_of_all_people = 0

for _ in range(number_of_groups_eq_loops):
    people_in_group = int(input())
    if people_in_group < 6:
        p1 += people_in_group
    elif 6 <= people_in_group <= 12:
        p2 += people_in_group
    elif 13 <= people_in_group <= 25:
        p3 += people_in_group
    elif 26 <= people_in_group <= 40:
        p4 += people_in_group
    else:
        p5 += people_in_group
    sum_of_all_people += people_in_group

print(f"{(p1 / sum_of_all_people * 100):.2f}%")
print(f"{(p2 / sum_of_all_people * 100):.2f}%")
print(f"{(p3 / sum_of_all_people * 100):.2f}%")
print(f"{(p4 / sum_of_all_people * 100):.2f}%")
print(f"{(p5 / sum_of_all_people * 100):.2f}%")
