n = int(input())
lst = [str(x) for x in input().split(",")]
slk = {}
for x in range(n):
    slk[x] = [int(0) for i in range(n)]

for x in lst:
    slk[int(x[0])][int(x[1])] = 9

for x in range(n):
    for y in range(n):
        if slk[x][y] == 9:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i + x == n or i + x == -1 or j + y == -1 or j + y == n:
                        pass
                    elif i == 0 and j == 0:
                        pass
                    else:
                        if slk[x+i][y+j] ==9:
                            pass
                        else:
                            slk[x+i][y+j] += 1
        else:
            pass
for x in slk:
    print(" ".join([str(i) for i in slk[x]]))