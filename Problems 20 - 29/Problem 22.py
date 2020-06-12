file = open("p022_names.txt", "r")

names = sorted(file.read().replace('"', '').split(","))

alphabetDict = {}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in alphabet:
    alphabetDict[i] = (alphabet.index(i) + 1)

value = 0
total = 0

for pos, name in enumerate(names):
    value = 0
    for letter in name:
        value += alphabetDict[letter]
    score = value * (pos + 1)
    total += score

print(total)
