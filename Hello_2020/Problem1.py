input()
n = input().split()
m = input().split()
z = int(input())
for a in range(z):
    year = int(input())
    res = ''
    if year%len(n) == 0:
        res += n[-1]
    else:
        res += n[year%len(n)-1]
    if year%len(m) == 0:
        res += m[-1]
    else:
        res += m[year%len(m)-1]
    print(res)
    