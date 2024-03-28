a = list(map(str, input()))
t = 0
for i in range(len(a)):
    if(a[i] == 'A' or a[i] == 'B' or a[i] == 'C'):
        t = t + 3
    elif(a[i] == 'D' or a[i] == 'E' or a[i] == 'F'):
        t = t + 4
    elif(a[i] == 'G' or a[i] == 'H' or a[i] == 'I'):
        t = t + 5
    elif(a[i] == 'J' or a[i] == 'K' or a[i] == 'L'):
        t = t + 6
    elif(a[i] == 'M' or a[i] == 'N' or a[i] == 'O'):
        t = t + 7
    elif(a[i] == 'P' or a[i] == 'Q' or a[i] == 'R' or a[i] == 'S'):
        t = t + 8
    elif(a[i] == 'T' or a[i] == 'U' or a[i] == 'V'):
        t = t + 9
    elif(a[i] == 'W' or a[i] == 'X' or a[i] == 'Y' or a[i] == 'Z'):
        t = t + 10
print(t)