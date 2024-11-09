n = int(input())
m = int(input())
li = []
t = 0

for i in range(n, m+1):
    if i > 1:
        a = True
        for j in range(2, i):
            if i % j == 0:
                a = False
                break
        if a:
            li.append(i)
            t = t + i
            
if len(li) > 0:
    print(t)
    print(li[0])
else:
    print(-1)
