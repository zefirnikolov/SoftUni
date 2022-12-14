number = int(input())

counter = 0

for i in range(number + 1):
    for j in range(number + 1):
        for k in range(number + 1):
            total_sum = i + j + k
            if total_sum == number:
                counter += 1

print(counter)
