num = int(input())

for i in range(1, 10):

    for j in range(1, 10):

        for k in range(1, 10):

            for h in range(1, 10):
                if num % i == 0 and num % j == 0 and num % k == 0 and num % h == 0:
                    print(f"{i}{j}{k}{h}", end=" ")
