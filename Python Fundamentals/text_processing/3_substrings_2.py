def remover(first, second):
    while True:
        if first not in second:
            break

        second = second.replace(first, '')
    return second


string_to_remove = input()
word = input()
print(remover(string_to_remove, word))
