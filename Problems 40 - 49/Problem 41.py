def isPandigital(number):
    numList = []
    digitList = []
    for n in range(1, len(str(number)) + 1):
        numList.append(n)
    for i in str(number):
        digitList.append(int(i))
    if sorted(digitList) == numList:
        return True
    else:
        return False


def isPrime(n):
    if n < 2:
        return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True


for y in reversed(range(1, 7654321)):
    if isPrime(y) and isPandigital(y):
        print(y)
        break


