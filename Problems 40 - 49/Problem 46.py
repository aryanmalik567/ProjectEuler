def isPrime(num):
    if num < 2:
        return False
    for x in range(2, int(num**0.5) + 1):
        if num % x == 0:
            return False
    return True


n = 9
end = False

while not end:
    if not isPrime(n):
        for s in range(1, int(n ** 0.5) + 1):
            p = n - (2 * s**2)
            if p < 0:
                end = True
                print(n)
                break
            elif isPrime(p):
                n += 2
                break
    else:
        n += 2
