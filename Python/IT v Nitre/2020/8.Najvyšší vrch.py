y, x = [int(x) for x in input().split()]
slk = {}
lst = []
ct = 0
for i in range(y):
	slk[i] = [int(x) for x in input().split()]
	lst.append(max(slk[i]))
for i in slk:
	if max(lst) in slk[i]:
		for j in slk[i][::-1]:
			ct+=1
			if j ==max(lst):
				break
		print(f"{i} {x-ct}")
		break