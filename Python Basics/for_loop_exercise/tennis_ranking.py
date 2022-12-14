num_of_tournaments_eq_loops = int(input())
score = int(input())

tournament_counter = 0
won_counter = 0
starting_score = score

for _ in range(num_of_tournaments_eq_loops):
    stage_reached = input()

    if stage_reached == "W":
        score += 2000
        won_counter += 1
    elif stage_reached == "F":
        score += 1200
    else:
        score += 720

    tournament_counter += 1


print(f"Final points: {score}")
print(f"Average points: {(score - starting_score) // tournament_counter}")
print(f"{(won_counter / tournament_counter * 100):.2f}%")
