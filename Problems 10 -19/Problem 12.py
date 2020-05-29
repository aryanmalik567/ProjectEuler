end = False


def factors(num):
    divisors = []
    for n in range(1, int(num**0.5) + 1):
        if num % n == 0:
            divisors.append(n)
            divisors.append(num/n)
    return divisors


def triangleNumber(nth):
    result = 0
    for n in range(1, nth + 1):
        result += n
    return result


term = 1
while not end:
    if len(factors(triangleNumber(term))) > 500:
        end = True
        print(triangleNumber(term))
    else:
        term += 1
