import math

eratosthenes = []
number = 2000000

for n in range(2, number + 1):
    eratosthenes.append(n)

prime = 2

while prime <= int(math.sqrt(number)):
    if prime in eratosthenes:
        for i in range(2*prime, number + 1, prime):
            eratosthenes[i-2] = 0

    prime += 1

print(sum(eratosthenes))
