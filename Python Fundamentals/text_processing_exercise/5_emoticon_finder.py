def emoticon_finder(data):
    results = ''
    for index in range(len(data)):
        if data[index] == ":":
            results += data[index] + data[index + 1] + "\n"
    return results


text = input()
print(emoticon_finder(text))
