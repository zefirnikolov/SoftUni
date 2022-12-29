values = input().split("|")
budget = float(input())

ticket_price = 150
total_sum_of_new_prices = 0
remaining_budget = budget
profit = 0

for elem in values:
    new_list = elem.split("->")
    type_of_item = ''

    for element in new_list:
        if element == "Clothes":
            type_of_item = "Clothes"
            continue
        elif element == "Shoes":
            type_of_item = "Shoes"
            continue
        elif element == "Accessories":
            type_of_item = "Accessories"
            continue

        if type_of_item == "Clothes" and float(element) <= 50:

            if remaining_budget - float(element) < 0:
                continue
            profit += float(element) * 0.4
            remaining_budget -= float(element)
            increased_item = float(element) + float(element) * 0.4
            total_sum_of_new_prices += increased_item
            print(f"{increased_item:.2f}", end=" ")

        if type_of_item == "Shoes" and float(element) <= 35:

            if remaining_budget - float(element) < 0:
                continue
            profit += float(element) * 0.4
            remaining_budget -= float(element)
            increased_item = float(element) + float(element) * 0.4
            total_sum_of_new_prices += increased_item
            print(f"{increased_item:.2f}", end=" ")

        if type_of_item == "Accessories" and float(element) <= 20.5:

            if remaining_budget - float(element) < 0:
                continue
            profit += float(element) * 0.4
            remaining_budget -= float(element)
            increased_item = float(element) + float(element) * 0.4
            total_sum_of_new_prices += increased_item
            print(f"{increased_item:.2f}", end=" ")

print()
print(f"Profit: {profit:.2f}")
if remaining_budget + total_sum_of_new_prices >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
