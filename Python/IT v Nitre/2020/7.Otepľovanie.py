lst = [float(x) for x in input().split()]
a = 1
b=1
for x in range(len(lst)):
	if x == len(lst)-1:
		break
	elif lst[x]<lst[x+1]:
		a +=1
	else:
		if a>b:
			b = a
		a = 1
print(max(a,b))