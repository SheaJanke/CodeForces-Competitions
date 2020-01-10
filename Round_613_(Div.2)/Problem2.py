def isHappy(vals):
    front = 0
    back = 0
    for a in range(len(vals)):
        front -= vals[a]
        if front >= 0:
             return 'NO'      
    for b in range(len(vals)-1,-1,-1):
        back -= vals[b]
        if back >= 0:
            return "NO"
    return 'YES'

n = int(input())
for a in range(n):
    input()
    vals = list(map(int,input().split()))
    print(isHappy(vals))