lst = [str(x) for x in input()]
n = input()
samohlasky = ["a","e","i","o","u","y"]
for x in range(len(lst)):
	if lst[x] in samohlasky:
		if lst[x] == "i":
			if x != len(lst) - 1:
				if lst[x+1] in samohlasky:
					lst[x+1] = n
				else:
					lst[x] = n
			else:
				lst[x] = n
		else:
			lst[x] = n
print("".join(lst))