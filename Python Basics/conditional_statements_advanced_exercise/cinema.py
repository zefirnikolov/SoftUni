type_of_ticket = input()
rows = int(input())
columns = int(input())

price = 0

if type_of_ticket == "Premiere":
    price = 12
elif type_of_ticket == "Normal":
    price = 7.5
elif type_of_ticket == "Discount":
    price = 5

full_cinema_profit = rows * columns * price

print(f"{full_cinema_profit:.2f} leva.")
