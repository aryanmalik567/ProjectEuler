nineList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pandigitals = [1]
end = False


for integer in range(9123, 9876):

    product = 100000 * integer + 2 * integer
    productDigits = []
    for i in str(product):
        productDigits.append(int(i))
    if sorted(productDigits) == nineList:
        pandigitals.append(product)

print(pandigitals)
