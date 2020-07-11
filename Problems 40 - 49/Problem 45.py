def isPentagonal(n):
    if ((24*n + 1)**0.5 + 1) % 6 == 0:
        return True
    else:
        return False


def isHexagonal(n):
    if ((8*n + 1)**0.5 + 1) % 4 == 0:
        return True
    else:
        return False


specialNumbers = []
x = 1
while len(specialNumbers) < 3:
    T = x*(x+1) / 2
    if isPentagonal(T) and isHexagonal(T):
        specialNumbers.append(int(T))
    x += 1

print(specialNumbers)
