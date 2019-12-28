input()
give = input().split()
recieve = [False]*len(give)
toFill = []
for a in range(len(give)):
    if give[a] != '0':
        recieve[int(give[a])-1] = True
    else:
        toFill.append(a)
a = 0
while a < len(toFill):
    if recieve[toFill[a]] == False:
        place = recieve.index(False)
        if place != toFill[a]:
            give[toFill[a]] = str(place+1)
            recieve[place] = True
            toFill.remove(toFill[a])
            a-=1
    a+=1
for a in toFill: 
    place = recieve.index(False)
    give[a] = str(place+1)
    recieve[place] = True
result = ''
for a in give:
    result += a + ' '
print(result)

