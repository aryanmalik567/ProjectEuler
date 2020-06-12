def d(n):
    divisors = []
    for x in range(1, (n // 2 + 1)):
        if n % x == 0:
            divisors.append(x)
    return sum(divisors)


amicables = []

for a in range(1, 10000):
    b = d(a)
    if d(b) == a and a != b:
        amicables.append(a)

print(sum(amicables))
