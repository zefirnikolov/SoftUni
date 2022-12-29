lesson_list = input().split(", ")

while True:

    command = input()

    if command == "course start":
        break

    action_list = command.split(":")
    current_action = action_list[0]
    lesson_title = action_list[1]
    is_lesson_exists = False

    if lesson_title in lesson_list:
        is_lesson_exists = True

    if is_lesson_exists == False and current_action == "Add":
        lesson_list.append(lesson_title)
    elif is_lesson_exists == False and current_action == "Insert":
        lesson_list.insert(int(action_list[2]), lesson_title)
    elif is_lesson_exists and current_action == "Remove":
        lesson_list.remove(lesson_title)
    elif is_lesson_exists and current_action == "Exercise":
        new_element = lesson_title + "-Exercise"
        if new_element not in lesson_list:
            new_element_index = lesson_list.index(lesson_title) + 1  # possible pitfall is lesson_title is on last index
            # if len(lesson_list) != lesson_list[-1]:
            lesson_list.insert(new_element_index, new_element)
            # else:
            #     lesson_list.append(new_element)
    elif is_lesson_exists == False and current_action == "Exercise":
        lesson_list.append(lesson_title)
        new_element = lesson_title + "-Exercise"
        lesson_list.append(new_element)
    elif is_lesson_exists and current_action == "Swap":
        if action_list[2] in lesson_list:
            index_one = lesson_list.index(lesson_title)
            index_two = lesson_list.index(action_list[2])
            lesson_list[index_one], lesson_list[index_two] = lesson_list[index_two], lesson_list[index_one]
        check_exercise_one = lesson_title + "-Exercise"
        check_exercise_two = action_list[2] + "-Exercise"
        if check_exercise_one in lesson_list:
            lesson_list.remove(check_exercise_one)
            new_element_index = lesson_list.index(lesson_title) + 1
            lesson_list.insert(new_element_index, check_exercise_one)
        elif check_exercise_two in lesson_list:
            lesson_list.remove(check_exercise_two)
            new_element_index = lesson_list.index(action_list[2]) + 1
            lesson_list.insert(new_element_index, check_exercise_two)

for index, element in enumerate(lesson_list):
    print(f"{index + 1}.{element}")
