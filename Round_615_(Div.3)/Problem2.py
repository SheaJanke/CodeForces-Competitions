n = int(input())
for a in range(n):
    boxes = int(input())
    height = 0
    positions = {}
    result = ""
    currentX = 0
    currentY = 0
    works = True
    for b in range(boxes):
        xy = list(map(int,input().split()))
        if xy[1] > height:
            height = xy[1]
        if xy[1] in positions:
            positions[xy[1]].append(xy[0])
        else:
            positions[xy[1]] = [xy[0]]
    for b in range(0,height+1):
        if b in positions:
            positions[b] = sorted(positions[b])
            if positions[b][0] < currentX:
                print("NO")
                works = False
                break
            else:
                result += "R" * (positions[b][0]-currentX) + "U" * (b-currentY)
                currentX = positions[b][0]
                result += "R" * (positions[b][-1]-currentX)
                currentX = positions[b][-1]
                currentY = b
    if works == True:
        print("YES")
        print(result)