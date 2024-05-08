total = []
avg = 0

for i in range(5):
    score = int(input())
    if score < 40:
        total.append(40)
    else:
        total.append(score)
        
for j in range(5):
    avg += total[j]
avg = avg / 5
print("%d" % avg)