happiness_level = list(map(int, input().split()))
multiply = int(input())
multiplied_list = [element * multiply for element in happiness_level]
# multiplied_list = []
# for element in happiness_level:
#     new_element = element * multiply
#     multiplied_list.append(new_element)

happy_counter = 0
for element_2 in multiplied_list:
    if element_2 >= sum(multiplied_list) / len(multiplied_list):
        happy_counter += 1

if happy_counter >= len(multiplied_list) / 2:
    print(f"Score: {happy_counter}/{len(multiplied_list)}. Employees are happy!")
else:
    print(f"Score: {happy_counter}/{len(multiplied_list)}. Employees are not happy!")
