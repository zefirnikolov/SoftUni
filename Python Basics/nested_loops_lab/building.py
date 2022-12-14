floors = int(input())
buildings_per_floor = int(input())

for floor_num in range(floors, 0, -1):

    for building_num in range(buildings_per_floor):
        if floor_num == floors:
            print(f"L{floor_num}{building_num}", end=" ")
        elif floor_num % 2 == 1:
            print(f"A{floor_num}{building_num}", end=" ")
        else:
            print(f"O{floor_num}{building_num}", end=" ")
    print()
