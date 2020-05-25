import math


def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num = 600851475143
primeFactors = []

for divisor in range(2, int(math.sqrt(num))):
    if num % divisor == 0 and isprime(divisor):
        primeFactors.append(divisor)

print(primeFactors)