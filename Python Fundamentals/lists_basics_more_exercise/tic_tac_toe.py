first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))
third_list = list(map(int, input().split()))

if first_list == [1, 1, 1] or second_list == [1, 1, 1] or third_list == [1, 1, 1]:
    print('First player won')
elif first_list[0] == second_list[0] == third_list[0] == 1:
    print('First player won')
elif first_list[1] == second_list[1] == third_list[1] == 1:
    print('First player won')
elif first_list[2] == second_list[2] == third_list[2] == 1:
    print('First player won')
elif first_list[0] == second_list[1] == third_list[2] == 1:
    print('First player won')
elif first_list[2] == second_list[1] == third_list[0] == 1:
    print('First player won')
elif first_list == [2, 2, 2] or second_list == [2, 2, 2] or third_list == [2, 2, 2]:
    print("Second player won")
elif first_list[0] == second_list[0] == third_list[0] == 2:
    print('Second player won')
elif first_list[1] == second_list[1] == third_list[1] == 2:
    print('Second player won')
elif first_list[2] == second_list[2] == third_list[2] == 2:
    print('Second player won')
elif first_list[0] == second_list[1] == third_list[2] == 2:
    print('Second player won')
elif first_list[2] == second_list[1] == third_list[0] == 2:
    print('Second player won')
else:
    print("Draw!")
