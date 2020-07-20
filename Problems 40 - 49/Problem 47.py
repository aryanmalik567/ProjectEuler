def dpf(n):  # DistinctPrimeFactors
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in factors:
                factors.append(i)
    if n > 1:
        factors.append(n)
    return len(factors)


end = False
num = 1

while not end:
    if dpf(num) == dpf(num+1) == dpf(num+2) == dpf(num+3) == 4:
        print(num)
        end = True
    num += 1
