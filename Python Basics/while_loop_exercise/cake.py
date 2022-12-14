width = int(input())
length = int(input())

cake_peaces = width * length

while cake_peaces >= 0:
    peaces_taken = input()

    if peaces_taken == "STOP":
        break

    int_peaces_taken = int(peaces_taken)
    cake_peaces -= int_peaces_taken

if cake_peaces >= 0:
    print(f"{cake_peaces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_peaces)} pieces more.")
