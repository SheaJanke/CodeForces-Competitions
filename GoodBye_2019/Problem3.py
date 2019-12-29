def XOR(values):
    current = format(values[0],'b')
    for a in range(1,len(values)):
        add = format(values[a],'b')
        dif = len(add) - len(current)
        if dif > 0:
            current = '0'*dif + current
        elif dif < 0:
            add = '0'*abs(dif) + add 
        for b in range(len(add)):
            if current[b] == add[b]:
                current = current[:b] + '0' + current[b+1:]
            else:
                current = current[:b] + '1' + current[b+1:]
    print(int(current,2))
    return current

cases = int(input())
for a in range(cases):
    input()
    vals = list(map(int,input().split()))
    