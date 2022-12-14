size_eggs = input()
color_eggs = input()
batches = int(input())

price = 0

if size_eggs == "Large":
    if color_eggs == "Red":
        price += batches * 16
    elif color_eggs == "Green":
        price += batches * 12
    else:
        price += batches * 9

elif size_eggs == "Medium":
    if color_eggs == "Red":
        price += batches * 13
    elif color_eggs == "Green":
        price += batches * 9
    else:
        price += batches * 7

else:
    if color_eggs == "Red":
        price += batches * 9
    elif color_eggs == "Green":
        price += batches * 8
    else:
        price += batches * 5

price *= 0.65

print(f"{price:.2f} leva.")
