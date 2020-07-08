def truncatables(num):
    digitList = []
    left_to_right = []
    right_to_left = []
    outputList = []

    for i in str(num):
        digitList.append(i)
        left_to_right.append(i)
        right_to_left.append(i)

    d = 1

    while d < len(digitList):
        del left_to_right[0]
        output1 = "".join(left_to_right)
        outputList.append(int(output1))

        del right_to_left[-1]
        output2 = "".join(right_to_left)
        outputList.append(int(output2))

        d += 1

    return outputList


def isPrime(n):
    if n < 2:
        return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True


integer = 10
truncatablePrimes = []

while len(truncatablePrimes) != 11:
    prime = True
    if isPrime(integer):
        rotations = truncatables(integer)

        for r in rotations:
            if not isPrime(r):
                prime = False
                break

        if prime:
            truncatablePrimes.append(integer)

    integer += 1

print(sum(truncatablePrimes))
