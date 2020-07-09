integers = [0]
n = 1

while len(integers) <= 1000000:
    for i in str(n):
        integers.append(int(i))
    n += 1

print(integers[1] * integers[10] * integers[100] * integers[1000] *
      integers[10000] * integers[100000] * integers[1000000])
