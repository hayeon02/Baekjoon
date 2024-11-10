n = int(input())
a = n

for i in range(n):
    print(" " * (a-1) + "*" * (2*i+1))
    a = a - 1