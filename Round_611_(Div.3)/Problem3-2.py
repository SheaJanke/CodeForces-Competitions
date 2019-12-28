input()
give = input().split()
left = list(range(1,len(give)+1))
for a in give:
    if a != '0':
        left.remove(int(a))
save = []
saveLeft = []
for a in range(len(give)):
    if give[a] == '0':
        if len(left) == 2:
            save = [] + give
            saveLeft = [] + left
        if a+1 == left[0]:
            try:
                give[a] = str(left[1])
                left.pop(1)
            except:
                save[a] = str(saveLeft[0])
                save[save.index('0')] = str(saveLeft[1])
                give = save
                left = saveLeft
        else:
            give[a] = str(left[0])
            left.pop(0)
result = ''
for a in give:
    result += a + ' '
print(result) 