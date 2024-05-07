num = int(input())
mars = []
mars_ascii = []

for i in range(num):
    mars = list(input().split())
    total = 0
    for j in mars:
        if '@' in j:
            total = total * 3
        elif '%' in j:
            total = total + 5
        elif '#' in j:
            total = total - 7
        else:
            total = total + float(j)
    print("%.2f" % total)