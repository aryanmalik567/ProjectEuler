file = open("p042_words.txt", "r")
words = file.read().replace('"', '').split(",")
triangleWords = []

alphabetDict = {}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in alphabet:
    alphabetDict[i] = (alphabet.index(i) + 1)


def wordValue(name):
    total = 0
    for letter in name:
        total += alphabetDict[letter]
    return total


def ifTriangle(number):
    n = 1
    triangle = 1
    while triangle < number:
        n += 1
        triangle = 0.5 * n * (n + 1)
    if triangle == number:
        return True
    else:
        return False


for word in words:
    if ifTriangle(wordValue(word)):
        triangleWords.append(word)

print(len(triangleWords))
