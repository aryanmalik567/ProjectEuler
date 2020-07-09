import math


def evenCount(number):
    if len(str(number)) % 2 == 0:
        return True
    else:
        return False


def isPalindrome(number):

    numberLst = []

    for n in str(number):
        numberLst.append(n)

    if evenCount(number):
        firstHalf = []
        lastHalf = []
        halfCount = len(numberLst) / 2

        for n in range(0, int(halfCount)):
            firstHalf.append(numberLst[n])
        for n in reversed(range(int(halfCount), len(numberLst))):
            lastHalf.append(numberLst[n])

        if firstHalf == lastHalf:
            return True
        else:
            return False

    else:
        firstHalf = []
        lastHalf = []

        halfCount = math.floor(len(numberLst) / 2)

        for n in range(0, int(halfCount)):
            firstHalf.append(numberLst[n])
        for n in reversed(range((int(halfCount) + 1), len(numberLst))):
            lastHalf.append(numberLst[n])

        if firstHalf == lastHalf:
            return True
        else:
            return False


palindromes = []

for x in range(100, 1000):
    for y in range(100, 1000):
        if isPalindrome(x*y):
            palindromes.append(x*y)

print(max(palindromes))
