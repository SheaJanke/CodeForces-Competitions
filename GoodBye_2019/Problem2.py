cases = int(input())
for a in range(cases):
    sol = False
    n = int(input())
    nums = list(map(int,input().split()))
    minimum = nums[0]
    minindex = 0
    maximum = nums[0]
    maxindex = 0
    for b in range(1,n):
        if nums[b] >= maximum:
            maximum = nums[b]
            maxindex = b
            if maximum-minimum >= abs(minindex-maxindex)+1:
                print("YES")
                print(min(minindex,maxindex)+1, max(minindex,maxindex)+1)
                sol = True
                break
        if nums[b] <= minimum:
            minimum = nums[b]
            minindex = b
            if maximum-minimum >= abs(minindex-maxindex)+1:
                print("YES")
                print(min(minindex,maxindex)+1, max(minindex,maxindex)+1)
                sol = True
                break
    if not sol:
        print("NO")
