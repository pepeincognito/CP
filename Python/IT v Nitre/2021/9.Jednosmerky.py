n = int(input())
zznm = {}
ct = 0
for x in range(n):
	zznm[x] = [int(x) for x in input().split()]
for x in zznm:
	for y in range(len(zznm[x])):
		if zznm[x][y] == 1 and zznm[y][x] ==0:
			ct +=1
print(ct)