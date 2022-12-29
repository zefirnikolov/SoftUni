def price_calculator(product: str, quantity: int):
    total_price = None
    if product == "coffee":
        total_price = quantity * 1.5
    elif product == "water":
        total_price = quantity * 1
    elif product == "coke":
        total_price = quantity * 1.4
    elif product == "snacks":
        total_price = quantity * 2
    return f"{total_price:.2f}"


type_of_purchase = input()
number_of_purchases = int(input())
print(price_calculator(type_of_purchase, number_of_purchases))
