cases = int(input())
for a in range(cases):
    input()
    nums = list(map(int,input().split()))
    sol = False
    for b in range(len(nums)-1):
        if abs(nums[b+1]-nums[b]) >= 2:
            print('YES')
            print(b+1,b+2)
            sol = True
            break
    if not sol:
        print('NO')