n = int(input())
m = list(map(int, input().split()))
t = 0

for i in range(n):
    a = True
    if m[i] > 1:
        for j in range(2, m[i]):
            if m[i] % j == 0:
                a = False
                break
        if a:
            t = t + 1
print(t)