interval = 2

diagonals = [3]

while len(diagonals) < 2000:
    if len(diagonals) % 4 == 0:
        interval += 2
        diagonals.append(diagonals[-1] + interval)
    else:
        diagonals.append(diagonals[-1] + interval)

print(sum(diagonals) + 1)
