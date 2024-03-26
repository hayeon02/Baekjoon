s = str(input())
ss = []
y = [0]*26


for j in s:
    t = ord(j)
    ss.append(t)

for u in range(ord('a'),ord('z')+1): #u: a~z까지의 ord 값
    for i in ss: #i: ss[i]의 ord값
        if(i == u):
            y[i-97] += 1

for a in range(len(y)):
    print(y[a],  end = " ")