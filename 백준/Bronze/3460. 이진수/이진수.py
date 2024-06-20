t = int(input())

for i in range(t):
    a = []
    n = int(input())
    n = list(bin(n))

    n = n[::-1]

    for q in range(len(n)):
        if(n[q] == '1'):
            a.append(q)
        
    print(*a)