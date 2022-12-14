name = input()

score = 0

for ch in name:
    if ch == "a":
        score += 1
    elif ch == "e":
        score += 2
    elif ch == "i":
        score += 3
    elif ch == "o":
        score += 4
    elif ch == "u":
        score += 5
else:
    print(score)
