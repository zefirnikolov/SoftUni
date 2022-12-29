tail = input()
body = input()
head = input()

# head, tail = tail, head
#
# meerkat = [tail, body, head]
#
# print(meerkat)
animal = [tail, body, head]
animal[0], animal[-1] = animal[-1], animal[0]

print(animal)
