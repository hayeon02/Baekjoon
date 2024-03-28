N = int(input()) #과목 개수
M = list(map(int, input().split())) #현재 성적
m = []

score = 0
for i in range(N):
    m = ( M[i] / max(M) * 100)
    score = score + m
    
score = score / N
print(score)