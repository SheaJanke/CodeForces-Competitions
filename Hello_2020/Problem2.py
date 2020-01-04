n = int(input())
ascentCount = 0
startEnd = []
count = 0
for a in range(n):
    values = list(map(int,input().split()[1:]))
    ascent = False
    for b in range(len(values)-1):
        if values[b] < values[b+1]:
            ascentCount += 1
            ascent = True
            break
    if ascent == False:
        vals = []
        vals.append(values[0])
        vals.append(values[-1])
        startEnd.append(vals)
count += ascentCount * n
count += (n-ascentCount) * ascentCount
for a in startEnd:
    for b in startEnd:
        if a[-1] < b[0]:
            count += 1
print(count)
