def sum_divisors(num):
    divs = []
    for x in range(1, (num // 2 + 1)):
        if num % x == 0:
            divs.append(x)
    return sum(divs)


def is_abundant(num):
    if sum_divisors(num) > num:
        return True
    else:
        return False


abundants = []
for n in range(1, 28124):
    if is_abundant(n):
        abundants.append(n)

abundants_set = set(abundants)


def abundant_sum(num):
    for x in abundants:
        if x > num:
            return False
        if (num - x) in abundants_set:
            return True
    return False


print(sum(x for x in range(1, 28124) if not abundant_sum(x)))
