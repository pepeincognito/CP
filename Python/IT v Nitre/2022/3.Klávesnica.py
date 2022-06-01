slk = {
	1:["a","d","g","j","m","p","t","w"],
	2:["b","e","h","k","n","q","u","x"],
	3:["c","f","i","l","o","r","v","y"],
	4:["s","z"]
}
ct = 0
for x in input():
	for i in range(1,5):
		if x in slk[i]:
			ct+=i
			break
			
print(ct)