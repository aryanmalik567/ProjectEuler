x = 1


def isprime(n):
    if n > 1:
        if n == 4:
            return False
        for i in range(2, n//2):
            if n % i == 0:
                return False
        return True
    else:
        return False


num = 1
n = 0

while n <= 10000:  # Where n is the nth prime
    if isprime(num):
        n += 1
    num += 1

print(str(n) + "th prime: " + str(num - 1))


