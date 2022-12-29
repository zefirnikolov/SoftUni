from math import ceil

persons_to_elevate = int(input())
elevator_capacity = int(input())

result = ceil(persons_to_elevate / elevator_capacity)

print(result)
