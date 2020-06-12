n = 0
end = False

fiblst = [1, 2]

while not end:
    x = fiblst[n]
    y = fiblst[n + 1]
    temp = x + y
    if temp < 4000000:
        fiblst.append(temp)
    else:
        end = True
    n += 1

evenLst = []

for n in fiblst:
    if n % 2 == 0:
        evenLst.append(n)

print(sum(evenLst))