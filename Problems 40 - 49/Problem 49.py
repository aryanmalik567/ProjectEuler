def isPrime(num):
    if num < 2:
        return False
    for x in range(2, int(num**0.5) + 1):
        if num % x == 0:
            return False
    return True


def perms(a, b, c):
    list1 = []
    list2 = []
    list3 = []
    for x, y, z in zip(str(a), str(b), str(c)):
        list1.append(int(x))
        list2.append(int(y))
        list3.append(int(z))

    if sorted(list1) == sorted(list2) == sorted(list3):
        return True
    else:
        return False


fourDigitPrimes = []

for n in range(1000, 10000):
    if isPrime(n):
        fourDigitPrimes.append(n)

for p in fourDigitPrimes:
    for d in range(1, 5000):
        if (p + d) in fourDigitPrimes and (p + 2*d) in fourDigitPrimes:
            if perms(p, p + d, p + 2*d):
                print(p, p+d, p + 2*d)

