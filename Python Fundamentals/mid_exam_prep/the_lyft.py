people = int(input())
lyft_list = [int(num) for num in input().split()]
total_free_space = (len(lyft_list) * 4) - sum(lyft_list)


full_cabins = people // 4
remainder = people % 4


for i in range(1, len(lyft_list) + 1):
    if i <= full_cabins:
        lyft_list[i - 1] = 4

for index, element in enumerate(lyft_list):
    if element == 0:
        lyft_list[index] = remainder
        break


if total_free_space - people < 0:
    print(f"There isn't enough space! {people - total_free_space} people in a queue!")
    lyft_list =[str(x) for x in lyft_list]
    print(' '.join(lyft_list))
else:
    print(f"The lift has empty spots!")
    lyft_list =[str(x) for x in lyft_list]
    print(' '.join(lyft_list))
