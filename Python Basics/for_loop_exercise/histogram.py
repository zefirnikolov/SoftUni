number_of_loops = int(input())

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0

for _ in range(number_of_loops):
    current_number = int(input())

    if current_number < 200:
        counter1 += 1
    elif 200 <= current_number <= 399:
        counter2 += 1
    elif 400 <= current_number <= 599:
        counter3 += 1
    elif 600 <= current_number <= 799:
        counter4 += 1
    else:
        counter5 += 1

print(f"{(counter1 / number_of_loops * 100):.2f}%")
print(f"{(counter2 / number_of_loops * 100):.2f}%")
print(f"{(counter3 / number_of_loops * 100):.2f}%")
print(f"{(counter4 / number_of_loops * 100):.2f}%")
print(f"{(counter5 / number_of_loops * 100):.2f}%")
