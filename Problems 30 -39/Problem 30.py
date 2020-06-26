numbers = []

for n in range(1, 354294):
    total = 0
    for i in str(n):
        total += (int(i) ** 5)
    if total == n:
        numbers.append(n)

print(sum(numbers) - 1)
