name = input()

score = 0

for i in range(0, len(name)):
    if name[i] == "a":
        score += 1
    elif name[i] == "e":
        score += 2
    elif name[i] == "i":
        score += 3
    elif name[i] == "o":
        score += 4
    elif name[i] == "u":
        score += 5

print(score)
