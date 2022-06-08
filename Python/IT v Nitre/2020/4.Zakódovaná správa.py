numerals = [str(x) for x in range(1,10)]
n = input()
lst = []
for x in range(len(n)):
	if n[x] in numerals:
		lst.append(n[int(n[x])+x])
print("".join(lst))