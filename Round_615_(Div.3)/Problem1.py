n = int(input())
for a in range(n):
    values = list(map(int,input().split()))
    maximum =  values[0]
    total = 0
    for a in range(3):
        if values[a] > maximum:
            maximum = values[a]
        total += values[a]
    total += values[3]
    if total%3 == 0 and total/3 >= maximum:
        print("YES")
    else:
        print("NO")