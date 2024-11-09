N = int(input())
j = N

for i in range(N):
    print(" " * (j - 1) + "*" * (i+ 1))
    j = j - 1