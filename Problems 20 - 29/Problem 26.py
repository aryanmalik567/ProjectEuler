differences = []

for denominator in range(2, 1000):
    remainder = 1
    remainders = []
    currentIteration = 0
    end = False

    while not end:
        if denominator < remainder:
            temp = remainder % denominator

            if temp == 0:
                end = True
                break

            digit = int((remainder - temp) / denominator)
            remainder = temp

            if [remainder, digit] not in remainders:
                remainders.append([remainder, digit])
                currentIteration += 1
            else:
                pos = remainders.index([remainder, digit])
                differences.append([(currentIteration - pos), denominator])
                end = True

        else:
            remainder *= 10


print(max(differences))




