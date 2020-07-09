months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeap(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
    else:
        return False


sunCount = 0
day = 2  # 01/01/1901 was a Tuesday
week = 7

for year in range(1901, 2001):

    if isLeap(year):
        months[1] = 29
    else:
        months[1] = 28

    for month in months:
        dayCount = 1
        while dayCount <= month:
            if dayCount == 1 and day == 7:
                sunCount += 1
                dayCount += 1
                day = 1
            elif day == 7:
                dayCount += 1
                day = 1
            else:
                day += 1
                dayCount += 1


print(sunCount)

