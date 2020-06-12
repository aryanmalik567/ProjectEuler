def factorial(n):
    temp = n
    for x in range(1, n):
        temp *= x
    return temp


def sumDigits(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum


print(sumDigits(factorial(100)))
