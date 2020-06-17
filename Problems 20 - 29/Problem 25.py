def fibonacci(term):
    sequence = [1, 1]
    n = 1
    while len(sequence) < term:
        sequence.append(sequence[n] + sequence[n-1])
        n += 1
    return sequence[n]


end = False
term = 3
while not end:
    if len(str(fibonacci(term))) == 1000:
        end = True
        print(term)
    else:
        term += 1
