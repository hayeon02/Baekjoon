h = 0
t = 0
j = []

for i in range(10):
    j = list(map(int, input().split()))
    h = h + j[1]
    h = h - j[0]
    
    if(h > t):
        t = h
    
print(t)