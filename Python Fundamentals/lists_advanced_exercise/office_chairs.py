number_of_rooms_eq_loops = int(input())

total_chairs = 0
total_people = 0
is_all_rooms_ok = True

for room in range(1, number_of_rooms_eq_loops + 1):
    info_list = input().split()

    chairs_in_a_room = 0
    people_in_a_room = 0

    for element in info_list:
        if not element.isdigit():
            chairs_in_a_room = len(element)
            total_chairs += chairs_in_a_room
        else:
            people_in_a_room = int(element)
            total_people += people_in_a_room

    if chairs_in_a_room < people_in_a_room:
        print(f"{people_in_a_room - chairs_in_a_room} more chairs needed in room {room}")
        is_all_rooms_ok = False

if is_all_rooms_ok:
    print(f"Game On, {total_chairs - total_people} free chairs left")
