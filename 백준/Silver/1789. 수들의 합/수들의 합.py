s = int(input())
t = 0

for i in range(1, s+1):
    t = t + i
    if t > s:
        print(i-1)
        break
    elif t == s:
        print(i)
        break