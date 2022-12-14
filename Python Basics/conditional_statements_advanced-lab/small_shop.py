product = input()
city = input()
number_of_products = float(input())

if city == "Sofia":
    if product == "coffee":
        print(number_of_products * 0.5)
    elif product == "water":
        print(number_of_products * 0.8)
    elif product == "beer":
        print(number_of_products * 1.2)
    elif product == "sweets":
        print(number_of_products * 1.45)
    elif product == "peanuts":
        print(number_of_products * 1.6)

if city == "Plovdiv":
    if product == "coffee":
        print(number_of_products * 0.4)
    elif product == "water":
        print(number_of_products * 0.7)
    elif product == "beer":
        print(number_of_products * 1.15)
    elif product == "sweets":
        print(number_of_products * 1.3)
    elif product == "peanuts":
        print(number_of_products * 1.5)

if city == "Varna":
    if product == "coffee":
        print(number_of_products * 0.45)
    elif product == "water":
        print(number_of_products * 0.7)
    elif product == "beer":
        print(number_of_products * 1.1)
    elif product == "sweets":
        print(number_of_products * 1.35)
    elif product == "peanuts":
        print(number_of_products * 1.55)
