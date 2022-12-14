number_of_balls_eq_loops = int(input())

total_points = 0
red_balls_counter = 0
orange_balls_counter = 0
yellow_balls_counter = 0
white_balls_counter = 0
black_balls_counter = 0
other_balls_counter = 0

for _ in range(number_of_balls_eq_loops):
    type_of_ball = input()

    if type_of_ball == "red":
        red_balls_counter += 1
        total_points += 5

    elif type_of_ball == "orange":
        orange_balls_counter += 1
        total_points += 10

    elif type_of_ball == "yellow":
        yellow_balls_counter += 1
        total_points += 15

    elif type_of_ball == "white":
        white_balls_counter += 1
        total_points += 20

    elif type_of_ball == "black":
        total_points //= 2
        black_balls_counter += 1

    else:
        other_balls_counter += 1

print(f"Total points: {total_points}")
print(f"Red balls: {red_balls_counter}")
print(f"Orange balls: {orange_balls_counter}")
print(f"Yellow balls: {yellow_balls_counter}")
print(f"White balls: {white_balls_counter}")
print(f"Other colors picked: {other_balls_counter}")
print(f"Divides from black balls: {black_balls_counter}")
