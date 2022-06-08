lst = [int(x) for x in input().split()]
vys = []
prim = 0
vyd = 0
pt = []
for x in range(0,len(lst)-1,2):
	vys.append(lst[x]-lst[x+1])
	prim += lst[x]
	vyd += lst[x-1]
if prim == vyd: pt.append("vyrovnany")
elif prim > vyd: pt.append("plus")
else: pt.append("minus")
pt.append(vys.index(min(vys))+1)
print(" ".join([str(x) for x in pt]))