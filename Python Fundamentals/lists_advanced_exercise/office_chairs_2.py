def check_chairs(num_rooms):
    total_free_chairs = 0
    needed_chairs = 0
    for room in range(1, num_rooms + 1):
        info_list = input().split()
        free_chairs = info_list[0]
        visitors = info_list[1]
        difference = len(free_chairs) - int(visitors)
        if difference >= 0:
            total_free_chairs += difference
        else:
            needed_chairs += abs(difference)
            print(f"{abs(difference)} more chairs needed in room {room}")
    return total_free_chairs, needed_chairs


number_of_rooms = int(input())
tot_free_chairs, need_chairs = check_chairs(number_of_rooms)
if tot_free_chairs >= need_chairs:
    print(f"Game On, {tot_free_chairs} free chairs left")
