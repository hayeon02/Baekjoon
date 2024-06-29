n = int(input())
pibo = []

for i in range(n+1):
    if i == 0:
        pibo.append(0)
    elif i == 1:
        pibo.append(1)
    else:
        f = pibo[i-1] + pibo[i-2]
        pibo.append(f)

print(pibo[n])