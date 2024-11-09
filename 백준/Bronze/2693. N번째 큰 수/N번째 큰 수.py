a = int(input())
li = []

for i in range(a):
    li.clear()
    li = list(map(int, input().split()))
    li.sort()
    print(li[7])