import sys

n = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(n):
    a = int(sys.stdin.readline())
    arr[a] += 1

for j in range(1, 10001):
    for q in range(arr[j]):
        print(j)