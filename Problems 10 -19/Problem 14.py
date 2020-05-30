def nextTerm(currentTerm):
    if currentTerm % 2 == 0:
        return int(currentTerm / 2)
    else:
        return int(3*currentTerm + 1)


lengths = []

for n in range(2, 1000000):
    sequence = [n]

    while n > 1:
        n = nextTerm(n)
        sequence.append(n)

    lengths.append(len(sequence))

max_value = max(lengths)

print(lengths.index(max_value) + 2)

