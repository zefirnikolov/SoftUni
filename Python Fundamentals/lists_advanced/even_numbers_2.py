numbers = input().split(", ")

int_numbers = list(map(int, numbers))
indices = [i for i in range(len(int_numbers)) if int_numbers[i] % 2 == 0]
print(indices)
