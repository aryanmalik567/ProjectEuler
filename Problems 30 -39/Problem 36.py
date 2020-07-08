def isPalindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


doublePalindromes = []

for n in range(1, 1000000):
    if isPalindrome(n) and isPalindrome(bin(n)[2:]):
        doublePalindromes.append(n)

print(sum(doublePalindromes))
