a = int(input())

for i in range(a):
    b, c = input().split()
    
    for r in range(len(c)):
        print(c[r] * int(b), end="")
    print()