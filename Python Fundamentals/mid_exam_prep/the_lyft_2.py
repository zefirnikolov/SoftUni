people = int(input())
lyft_list = [int(num) for num in input().split()]

for i in range(len(lyft_list)):
    can_load = min(4 - lyft_list[i], people)
    lyft_list[i] += can_load
    people -= can_load

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif len([cart for cart in lyft_list if cart < 4]) > 0:
    print("The lift has empty spots!")

print(' '.join(str(x) for x in lyft_list))
