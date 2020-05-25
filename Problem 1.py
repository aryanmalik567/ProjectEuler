lst = []
n = 1
x = 1
end = False

while not end:
    if 5 * n < 1000:
        lst.append(3 * n)
        lst.append(5 * n)
    elif 3 * n < 1000:
        lst.append(3 * n)
    else:
        end = True
    try:
        lst.remove(15 * x)
        x += 1
        n += 1
    except:
        n += 1

print(sum(lst))
