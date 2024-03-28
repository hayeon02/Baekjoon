a, b, c = list(map(int, input().split()))
t = [0] * 100
cost = 0

for i in range(3):
    s = list(map(int, input().split()))
    for j in range(s[0], s[1], 1):
        t[j] = t[j] + 1

for q in range(len(t)):
    if(t[q] == 1):
        cost = cost + a
    elif(t[q] == 2):
        cost = cost + (b*2)
    elif(t[q] == 3):
        cost = cost + (c*3)
        
print(cost)