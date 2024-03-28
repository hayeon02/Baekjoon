s = list(map(str, input()))
ss = []
y = [-1]*26
for i in range(len(s)):
    ss.append(s[i])
for j in range(len(s)):
    for q in range(97, 123, 1):
        if(ord(s[j]) == q):
            if(y[q-97] == -1):
                y[q-97] = j
for r in range(len(y)):
    print(y[r], end=" ")