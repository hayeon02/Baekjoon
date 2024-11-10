n = int(input())
a = 0

for j in range(n-1, -1, -1):
    print(" " * (a) + "*" * (2*j+1))
    a = a + 1