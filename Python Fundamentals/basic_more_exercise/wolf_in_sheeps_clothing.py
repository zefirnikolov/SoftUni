sheep_list = [x for x in input().split(", ")]

counter_sheep = 0

for i in range(len(sheep_list) - 1, -1, -1):
    element = sheep_list[i]
    if sheep_list[i] == "wolf" and counter_sheep == 0:
        print('Please go away and stop eating my sheep')
        break
    elif sheep_list[i] == "sheep":
        counter_sheep += 1
    else:
        break

if counter_sheep != 0:
    print(f"Oi! Sheep number {counter_sheep}! You are about to be eaten by a wolf!")
