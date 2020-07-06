def del_from_str(string, index):
    return string[:index] + string[(index + 1):]


curious_fractions = []


for denominator in range(10, 99):
    for numerator in range(10, denominator):
        numer = str(numerator)
        denom = str(denominator)
        cancel = False

        if numer[0] == denom[0]:
            cancel = True
            numer = del_from_str(numer, 0)
            denom = del_from_str(denom, 0)
        elif numer[0] == denom[1]:
            cancel = True
            numer = del_from_str(numer, 0)
            denom = del_from_str(denom, 1)
        elif numer[1] == denom[0]:
            cancel = True
            numer = del_from_str(numer, 1)
            denom = del_from_str(denom, 0)
        elif numer[1] == denom[1]:
            cancel = True
            numer = del_from_str(numer, 1)
            denom = del_from_str(denom, 1)

        if int(numer) != 0 and int(denom) != 0 and cancel is True:
            if numerator / denominator == int(numer) / int(denom):
                if numerator % 10 != 0 and denominator % 10 != 0:
                    curious_fractions.append([numerator, denominator])
        else:
            pass

top = 1
bottom = 1

for n in range(0, len(curious_fractions)):
    top *= curious_fractions[n][0]
    bottom *= curious_fractions[n][1]

print(top / bottom)
