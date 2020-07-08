def factorial(num):
    output = 1
    for x in range(1, num+1):
        output *= x
    return output


curiousNums = []

for n in range(1, 7*factorial(9)):
    total = 0
    for i in str(n):
        total += factorial(int(i))
    if n == total:
        curiousNums.append(n)

print(sum(curiousNums) - 3)
