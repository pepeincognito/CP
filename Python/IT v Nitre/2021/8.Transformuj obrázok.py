lst = [int(x) for x in input().split()]

y=lst[0]
x = lst[1]
zznm = {}
for i in range(y):
	zznm[i] = [int(x) for x in input().split(",")]
if input() =="x":
	for x in range(y-1,-1,-1):
		print(zznm[x])
else:
	for x in range(y):
		print(zznm[x][::-1])