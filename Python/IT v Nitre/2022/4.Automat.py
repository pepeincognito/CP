lst = [int(x) for x in input().split()]
nom = [200, 100, 50, 20, 10, 5, 2, 1]
t = int(float(input())*100)


def solve(lst, t):
	if t ==0:
		print(f"Tovar zaplateny. Zostatok: {','.join([str(x) for x in lst])}")
		return
	for x in range(8):
		if lst[x] != 0:
			if nom[x]<=t:
				lst[x]-=1
				t-=nom[x]
				return solve(lst, t)
	print(f"Chybaju ti mince. Treba este: {t/100}")
solve(lst,t)