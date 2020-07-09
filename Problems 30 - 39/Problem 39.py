number_of_solutions = []

for p in range(0, 1001, 2):  # p must be even
    solutions = []
    for a in range(1, int(p/2)):
        for b in range(a, int(p/2)):
            c = (a**2 + b**2) ** 0.5
            if a + b + c == p:
                solutions.append([a, b, c])
    number_of_solutions.append([len(solutions), p])

print(max(number_of_solutions))
