word = input()

backwards = ''

for i in range(len(word) - 1, -1, -1):
    backwards += word[i]

print(backwards)
