josephus_list = list(map(int, input().split()))
n = int(input())

new_list = []

counter = 0

index = 0
while not len(josephus_list) < 1:
    counter += 1

    if counter % n == 0:
        new_list.append(josephus_list.pop(index))
    else:
        index += 1

    if index >= len(josephus_list):
        index = 0

result = ','.join([str(x) for x in new_list])
print(f"[{result}]")
