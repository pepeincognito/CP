"""
4
1 1 1 0
1 1 1 1
1 1 1 1
0 1 0 1
"""
n = int(input())
slk = {}
zznm = []

for x in range(n):
    slk[x] = [int(x) for x in input().split()]
for x in slk:
    ct = 0
    for i in range(len(slk[x])):
        if slk[x][i] == 1 and slk[i][x] == 1 and i != x:
            ct += 1
    zznm.append(ct)
if max(zznm) == 0:
    print("nikto nema kamaratov")
else:
    print(f"osoba {zznm.index(max(zznm))}")
