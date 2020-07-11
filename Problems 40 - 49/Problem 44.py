def isPentagonal(n):
    if ((24*n + 1)**0.5 + 1) % 6 == 0:
        return True
    else:
        return False


found = False
x = 2

while not found:
    for y in range(1, x):
        k = x*(3*x - 1) / 2
        j = y*(3*y - 1) / 2

        if isPentagonal(k + j) and isPentagonal(k - j):
            found = True
            print(int(k - j))
    x += 1


