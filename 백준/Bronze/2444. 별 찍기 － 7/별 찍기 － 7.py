n = int(input())
a = n

for i in range(n):
    print(" " * (a-1) + "*" * (2*i+1))
    a = a - 1

a = 0
for j in range(i-1, -1, -1):
    print(" " * (a+1) + "*" * (2*j+1))
    a = a + 1