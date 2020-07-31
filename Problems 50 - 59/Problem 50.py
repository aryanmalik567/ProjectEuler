def prime_eratosthenes(n):
    prime_list = []
    outputList = []
    for i in range(2, n+1):
        if i not in prime_list:
            outputList.append(i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)
    return outputList


def isPrime(num):
    if num < 2:
        return False
    for x in range(2, int(num**0.5) + 1):
        if num % x == 0:
            return False
    return True


primes = prime_eratosthenes(5000)
sums = []

for i in range(len(primes)):
    for j in range(i, len(primes)):
        total = sum(primes[i:j])
        if total < 1000000:
            if isPrime(total):
                sums.append([j - i, total])
        else:
            break

print(max(sums))