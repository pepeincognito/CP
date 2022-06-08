import math
lst = [10]
n = int(input())
x = math.floor((n*0.8-math.floor(n/2))/4)
for i in range(5):
	lst.append(math.floor(n/2)+x*i)
	if i != 5:
		lst.append(60)
print(" ".join([str(x) for x in lst]))
