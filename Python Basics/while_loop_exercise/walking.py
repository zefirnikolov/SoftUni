steps_walked = input()

total_steps = 0
is_goal_reached = False
goal = 10000
difference = 0

while steps_walked != "Going home":
    int_steps_walked = int(steps_walked)
    total_steps += int_steps_walked
    if total_steps >= goal:
        is_goal_reached = True
        break

    steps_walked = input()

if steps_walked == "Going home":
    steps_to_home = int(input())
    total_steps += steps_to_home
    if total_steps >= goal:
        is_goal_reached = True

difference = abs(total_steps - goal)

if is_goal_reached:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
