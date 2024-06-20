n, k = map(int, input().split())
t = []

for i in range(n):
    i = i + 1
    if(n % i == 0):
        t.append(i)
    
if(len(t) >= k):
    print(t[k-1])
else:
    print(0)