chess = [1, 1, 2, 2, 2, 8]
a=[]
have = list(map(int,input().split()))

for i in range(len(chess)):
    a.append(chess[i] - have[i])

for j in range(len(a)):
    print(a[j], end = " ")