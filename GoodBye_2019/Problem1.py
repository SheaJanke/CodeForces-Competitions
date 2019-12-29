cases = int(input())
for a in range(cases):
    input()
    p1 = max(list(map(int,input().split())))
    p2 = max(list(map(int,input().split())))
    if p1 > p2:
        print("YES")
    else:
        print("No")
    