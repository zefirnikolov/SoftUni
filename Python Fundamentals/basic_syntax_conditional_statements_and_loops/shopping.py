budget = int(input())

shopping_until_end = input()

is_money_enough = True

while shopping_until_end != "End":
    int_shopping_until_end = int(shopping_until_end)
    budget -= int_shopping_until_end
    if budget < 0:
        is_money_enough = False
        break

    shopping_until_end = input()

if not is_money_enough:
    print("You went in overdraft!")
else:
    print('You bought everything needed.')
