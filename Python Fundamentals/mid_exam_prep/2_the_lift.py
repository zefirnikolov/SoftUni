people = int(input())
wagons_list = list(map(int, input().split()))

for index in range(len(wagons_list)):
    wagon = wagons_list[index]
    if wagon < 4:
        difference = 4 - wagon
        if not people < difference:
            wagons_list[index] += difference
            people -= difference
        else:
            wagons_list[index] += people
            people = 0
    else:
        continue

if people == 0 and wagons_list.count(4) == len(wagons_list):
    pass
elif people == 0:
    print('The lift has empty spots!')
else:
    print(f"There isn't enough space! {people} people in a queue!")

print(' '.join([str(x) for x in wagons_list]))
