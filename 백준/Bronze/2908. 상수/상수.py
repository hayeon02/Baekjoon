a, b = list(map(int, input().split()))

aa = int(str(a)[::-1])
bb = int(str(b)[::-1])

if (aa > bb):
    print(aa)
else:
    print(bb)