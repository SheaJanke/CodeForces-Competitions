n = int(input())
for a in range(n):
    [a,b,money] = list(map(int,input().split()))
    path = input()
    if(len(path) <= 1):
        print(1)
        continue
    i = len(path)-2
    last = path[i]
    while(i >= 0):
        if path[i] != last:
            if path[i] == "A":
                money -= b
            else:
                money -= a
            last = path[i]
        if last == "A":
            cost = a
        else:
            cost = b
        if cost > money:
            break
        i-=1
    print(i+2)
