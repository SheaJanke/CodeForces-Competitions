n = int(input())
for a in range(n):
    nx = list(map(int, input().split()))
    s = input()
    values = {}
    minBalance = 0
    maxBalance = 0
    count = 0
    for value in s:
        if value == '0':
            count += 1
            if count > maxBalance:
                maxBalance = count
        else:
            count -= 1
            if count < minBalance:
                minBalance = count
        if count in values:
            values[count] += 1
        else:
            values[count] = 1
    target = nx[1]
    answer = 0
    if target == 0:
        answer += 1
    if count > 0:
        while target >= minBalance:
            if target in values:
                answer += values[target]
            target -= count
    elif count < 0:
        while target <= maxBalance:
            if target in values:
                answer += values[target]
            target -= count
    else:
        if target >= minBalance and target <= maxBalance:
            answer = -1
        else:
            answer = 0
    print(answer)