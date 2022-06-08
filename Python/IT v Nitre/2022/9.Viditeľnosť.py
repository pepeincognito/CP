n = int(input())
slk = {}
for x in range(n):
    slk[x] = [int(x) for x in input().split()]
lst = []
ct = 0
for y in slk:
    for x in range(len(slk[y])):
        if slk[y][x] ==max(slk[y]) and slk[y][x] == max( [int(slk[i][x]) for i in range(n)]):
            lst.append([y,x])

print(lst)
#9/10 tests
#probably bad sample output