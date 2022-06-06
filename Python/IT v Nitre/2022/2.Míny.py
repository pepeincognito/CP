n = int(input())
lst = [str(x) for x in input().split()]
slk = {}
for x in range(n):
	slk[x] = [int(0) for i in range(n)]
	
for x in lst:
	slk[int(x[0])][int(x[1])] = 9

for x in range(n):
	for i in range(n):
		if slk[x][i] ==9:
			pass
		else:
			