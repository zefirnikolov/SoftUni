name_of_actor = input()
points = float(input())
number_of_juries_eq_loops = int(input())

is_nominated = False

for _ in range(number_of_juries_eq_loops):
    name_of_jury = input()
    score_from_jury = float(input())
    points += len(name_of_jury) * score_from_jury / 2

    if points > 1250.5:
        is_nominated = True
        break

if is_nominated:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {name_of_actor} you need {(1250.5 - points):.1f} more!")
