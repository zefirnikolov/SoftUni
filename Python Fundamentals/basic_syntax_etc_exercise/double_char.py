word = input()

while word != "End":

    if word == "SoftUni":
        word = input()
        continue

    for char in word:
        print(char, end="")
        print(char, end='')

    print()
    word = input()
