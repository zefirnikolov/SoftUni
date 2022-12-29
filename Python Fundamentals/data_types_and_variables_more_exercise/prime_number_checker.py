def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


number_input = int(input())
print(is_prime(number_input))
