from itertools import permutations

digits = [0, 1, 2]

perms = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

ansLst = perms[999999]
ans = ""

for i in ansLst:
    ans += str(i)

ans = int(ans)

print(ans)

