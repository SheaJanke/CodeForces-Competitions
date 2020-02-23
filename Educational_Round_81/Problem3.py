def smallestLarger(arr, target):
    a = 0
    while a < len(arr) and arr[a] < target:
        a+=1
    if a == len(arr):
        return -1
    return arr[a] 


n = int(input())
for a in range(n):
    s = input()
    t = input()
    values = {}
    for b in range(len(s)):
        if s[b] in values:
            values[s[b]].append(b)
        else:
            values[s[b]] = [b]
    operations = 0
    currentIndex = 0
    for b in t:
        if b not in values:
            print(-1)
        else:
            val = smallestLarger(values[b],currentIndex)
            if val == -1:
                operations += 1
                currentIndex = 0
                val = smallestLarger(values[b],currentIndex)
                currentIndex = val + 1
            else:
                currentIndex = val + 1
    if s != t:
        print(operations + 1)
        