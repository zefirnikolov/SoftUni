race_input = [int(x) for x in input().split()]

first_racer = race_input[:len(race_input)//2:]
second_racer = race_input[len(race_input)//2 + 1::]
first_racer_time = 0
second_racer_time = 0

for index in range(len(first_racer)):
    first_racer_time_eq_element = first_racer[index]
    if first_racer_time_eq_element == 0:
        first_racer_time *= 0.8
    first_racer_time += first_racer_time_eq_element

for index in range(len(second_racer) - 1, -1, -1):
    second_racer_time_eq_element = second_racer[index]
    if second_racer_time_eq_element == 0:
        second_racer_time *= 0.8
    second_racer_time += second_racer_time_eq_element

if first_racer_time < second_racer_time:
    print(f"The winner is left with total time: {first_racer_time:.1f}")
else:
    print(f"The winner is right with total time: {second_racer_time:.1f}")
