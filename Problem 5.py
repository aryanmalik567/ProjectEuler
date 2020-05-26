from math import gcd

numbers = []

for n in range(1, 21):
    numbers.append(n)

lcm = numbers[0]

for x in numbers:
    lcm = int(lcm * x) / gcd(int(lcm), x)

print(lcm)
