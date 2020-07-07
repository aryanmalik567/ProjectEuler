def circulars(num):
    digitList = []
    outputList = []
    n = 0
    for i in str(num):
        digitList.append(i)
    while n < len(str(num)):
        digitList.append(digitList[0])
        digitList.pop(0)
        output = "".join(digitList)
        outputList.append(int(output))
        n += 1

    return outputList


def isPrime(num):
    if num < 2:
        return False
    for x in range(2, int(num**0.5) + 1):
        if num % x == 0:
            return False
    return True


primes = []

for integer in range(1, 1000000):
    if isPrime(integer):
        primes.append(integer)


circularPrimes = []

for i in primes:
    rotations = circulars(i)
    prime = True
    index = 0
    while prime and index < len(rotations):
        if isPrime(rotations[index]):
            index += 1
        else:
            prime = False

    if prime is True:
        circularPrimes.append(i)

print(len(circularPrimes))
