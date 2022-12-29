number = int(input())

for i in range(97, number + 97):

    for k in range(97, number + 97):

        for j in range(97, number + 97):
            print(chr(i) + chr(k) + chr(j))
