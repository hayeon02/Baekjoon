n, k = map(int, input().split())
arr = []
d = []

for i in range(2, n+1):
    arr.append(i)
    
while arr:
    p = arr[0]
    
    for j in arr:
        if j % p == 0:
            d.append(j)
            arr.remove(j)

print(d[k-1])