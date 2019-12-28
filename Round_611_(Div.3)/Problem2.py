n = int(input())
for a in range(n):
    values = input().split()
    kids = int(values[1])
    candies = int(values[0])
    each = candies//kids
    if(candies % kids <= kids//2):
        print(candies)
    else:
        print(kids*each + kids//2)