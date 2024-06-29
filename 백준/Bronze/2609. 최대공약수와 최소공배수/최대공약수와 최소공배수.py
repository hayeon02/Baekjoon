a, b = map(int, input().split())

def div():
    a_div = []
    b_div = []
    ab_div = []

    for i in range(a):
        i = i + 1
        if(a % i == 0):
            a_div.append(i)

    for i in range(b):
        i = i + 1
        if(b % i == 0):
            b_div.append(i)

    ab_div = set(a_div) & set(b_div)
        
    print(max(ab_div))

def mul():
    a_mul = []
    b_mul = []
    ab_mul = [0]
    j = 1
    
    while True:
        a_mul.append(a*j)
        b_mul.append(b*j)
        
        if (set(a_mul) & set(b_mul) != set()):
            ab_mul = set(a_mul) & set(b_mul)
            break;
        else:
            j += 1
    print(min(ab_mul))
    
    
div()
mul()