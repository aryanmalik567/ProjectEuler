def consecutiveNum(number):

    output = []

    for n in range(1, number + 1):
        output.append(n)

    return output


products = []

for a in range(1, 100):
    for b in range(1, 10000):
        c = a*b
        testList = []

        for x in str(a):
            testList.append(int(x))
        for y in str(b):
            testList.append(int(y))
        for z in str(c):
            testList.append(int(z))

        if sorted(testList) == consecutiveNum(9):
            if c not in products:
                products.append(c)

print(sum(products))




