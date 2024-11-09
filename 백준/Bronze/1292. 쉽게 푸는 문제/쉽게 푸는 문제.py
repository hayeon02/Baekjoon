A, B = map(int,input().split())
listt = []
T = 0

for i in range(B+1):
    for j in range(i):
        listt.append(i)

for q in range(A, B+1):
    T =  T + listt[q-1]

print(T)