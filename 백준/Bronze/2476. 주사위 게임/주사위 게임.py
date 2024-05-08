num = int(input())
total = 0
money = 0
for i in range(num):
    a, b, c = map(int, input().split())
    d = [a, b, c]
    if a == b and b == c:
        total = 10000 + (a * 1000)
        if money < total:
            money = total
    elif a == b or a == c:
        total = 1000 + (a * 100)
        if money < total:
            money = total
    elif b == c or b == a:
        total = 1000 + (b * 100)
        if money < total:
            money = total
    else:
        total = max(d) * 100
        if money < total:
            money = total
print(money)
