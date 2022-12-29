from sys import maxsize

max_number = -maxsize

for _ in range(3):
    n = int(input())

    if n > max_number:
        max_number = n

print(max_number)
