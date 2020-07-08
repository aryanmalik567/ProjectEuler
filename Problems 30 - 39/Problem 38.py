def consecutiveNum(number):
    output = []
    for i in range(1, number + 1):
        output.append(i)
    return output


n = 1
integer = 1
pandigital = 1
while len(str(pandigital)) < 10:
    multipliers = []
    for multiplier in range(1, n):
        multipliers.append(multiplier)