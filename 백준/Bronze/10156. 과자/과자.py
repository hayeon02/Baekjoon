K, N, M = map(int, input().split())
total = (K * N) - M
if total < 0:
    total = 0
    
print(total)