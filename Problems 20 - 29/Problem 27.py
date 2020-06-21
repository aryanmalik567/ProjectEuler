def isPrime(num):
    if num < 2:
        return False
    for x in range(2, int(num**0.5) + 1):
        if num % x == 0:
            return False
    return True


lens = []

for a in range(-999, 1000):
    for b in range(-1000, 1001):

        prime = True
        n = 0
        primes = []

        while prime:
            number = n**2 + a*n + b

            if isPrime(number):
                primes.append(number)
                n += 1
            else:
                prime = False
                lens.append([len(primes), a, b])

print(max(lens))
