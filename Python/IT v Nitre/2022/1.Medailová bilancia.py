n = int(input())
slk = {}
sct = {}
for x in range(n):
	slk[x] = [int(x) for x in input().split(",")]
	sct[3*slk[x][0]+2*slk[x][1]+1*slk[x][2]] = x
lst = sorted(sct.keys())[::-1]

for x in lst:
	print(slk[sct[x]])