n = int(input())
slk = {}
for x in range(n):
    lst = input().split()
    a = int(lst[0])
    c = int(lst[2])
    b = lst[1]

    if a in slk:
        if c > slk[a][0]:
            slk[a] = c,b
    else:
        slk[a] = c,b
for x in slk:
    print(slk[x][1])