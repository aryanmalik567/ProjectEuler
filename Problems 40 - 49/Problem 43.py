import itertools

pandigitals = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
primes = [2, 3, 5, 7, 11, 13, 17]

specials = []

for pandigital in pandigitals:
    end = False
    for d, prime in zip(range(1, 8), primes):
        if not end:
            if ((pandigital[d] * 100) + (pandigital[d+1] * 10) + pandigital[d+2]) % prime == 0:
                if d == 7:
                    output = "".join(str(i) for i in pandigital)
                    specials.append(int(output))
            else:
                end = True

print(sum(specials))


