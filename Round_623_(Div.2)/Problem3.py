n = int(input())
for a in range(n):
    answer = ""
    size = int(input())
    nums = list(map(int,input().split()))
    taken = set(nums)
    possible = True
    if 1 not in taken:
        print(-1)
        continue
    for num in nums:
        answer += str(num) + " "
        found = False
        for b in range(num+1,2*size+1):
            if b not in taken:
                found = True
                taken.add(b)
                answer += str(b) + " "
                break
        if not found:
            possible = False
            break
    if possible:
        print(answer)
    else:
        print(-1)
