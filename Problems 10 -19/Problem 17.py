def num_to_words(number):
    switcher = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }

    if number < 20:
        return switcher[number]
    elif number < 100:
        digitLst = []

        for n in str(number):
            digitLst.append(int(n))

        tens = digitLst[0] * 10
        ones = digitLst[1]

        outputLst = [switcher[tens], switcher[ones]]

        return "".join(outputLst)
    elif number < 1000:
        digitLst = []

        for n in str(number):
            digitLst.append(int(n))

        hundreds = switcher[digitLst[0]] + "hundred"
        tens = "and" + switcher[digitLst[1] * 10]
        ones = switcher[digitLst[2]]

        if digitLst[1] == 0 and digitLst[2] == 0:
            tens = ""
        elif number - (digitLst[0] * 100) < 20:
            tens = "and" + switcher[number - (digitLst[0] * 100)]
            ones = ""

        return hundreds + tens + ones
    elif number == 1000:
        return "onethousand"


count = 0
for n in range(1, 1001):
    count += len(num_to_words(n))

print(count)
