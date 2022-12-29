number_of_snowballs_eq_loops = int(input())

the_best_snowball = 0
best_weight = 0
best_time = 0
best_quality = 0

for _ in range(number_of_snowballs_eq_loops):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality

    if value > the_best_snowball:
        best_weight = weight
        best_time = time
        best_quality = quality
        the_best_snowball = value

print(f"{best_weight} : {best_time} = {int(the_best_snowball)} ({best_quality})")
