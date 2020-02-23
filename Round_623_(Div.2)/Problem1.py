n = int(input())
for a in range(n):
    coords = list(map(int,input().split()))
    if coords[0] > 1:
        side = min(coords[2]+1,coords[0]-coords[2])*coords[1]
    else:
        side = coords[0]*coords[1]
    if coords[1] > 1:
        vert = min(coords[3]+1,coords[1]-coords[3])*coords[0]
    else:
        vert = coords[0]*coords[1]
    total = coords[0]*coords[1] - min(vert,side)
    print(total)