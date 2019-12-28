n = int(input())
for a in range(n):
    time = input().split()
    hours = int(time[0])
    mins = int(time[1])
    total = 0
    total += (23-hours)*60
    total += (60-mins)
    print(total)