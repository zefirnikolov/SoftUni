n1 = int(input())
n2 = int(input())
symbol = input()

if symbol == "+":
    ev_odd_sum = ''
    if (n1 + n2) % 2 == 0:
        ev_odd_sum = "even"
    else:
        ev_odd_sum = "odd"
    print(f"{n1} {symbol} {n2} = {n1 + n2} - {ev_odd_sum}")

elif symbol == "-":
    ev_odd_subs = ''
    if (n1 - n2) % 2 == 0:
        ev_odd_subs = "even"
    else:
        ev_odd_subs = "odd"
    print(f"{n1} {symbol} {n2} = {n1 - n2} - {ev_odd_subs}")

elif symbol == "*":
    ev_odd_product = ''
    if (n1 * n2) % 2 == 0:
        ev_odd_product = "even"
    else:
        ev_odd_product = "odd"
    print(f"{n1} {symbol} {n2} = {n1 * n2} - {ev_odd_product}")

elif symbol == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} / {n2} = {(n1 / n2):.2f}")

else:
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} % {n2} = {n1 % n2}")
