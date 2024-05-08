num = int(input())
total = []

for i in range(num):
    a, b, c = map(int, input().split())
    d = [a, b, c]
    if a == b and b == c:
        total.append(10000 + (a * 1000))
    elif a == b or a == c:
        total.append(1000 + (a * 100))
    elif b == c or b == a:
        total.append(1000 + (b * 100))
    else:
        total.append(max(d) * 100)
print(max(total))