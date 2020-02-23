n = int(input())
for a in range(n):
    value = int(input())
    if value % 2 ==0:
        print("1"*(value//2))
    else:
        print("7" + "1"*((value-3)//2))