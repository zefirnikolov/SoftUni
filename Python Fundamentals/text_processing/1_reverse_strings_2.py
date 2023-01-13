while True:
    text = input()
    if text == "end":
        break
    reverse = text[::-1]
    print(f"{text} = {reverse}")
