import itertools

a = []

for i in range(9):
    a.append(int(input()))

nCr = itertools.combinations(a, 7)
print("\n")
for i in nCr:
    if sum(i) == 100:
        s = list(i)
        s.sort()
        for h in range(len(s)):
            print(s[h])
        break