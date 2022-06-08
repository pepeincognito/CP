zznm = {}
n = input()
stlpec = n[0]
abc = ["a", "b", "c", "d", "e", "f", "g", "h"]
stlpec = abc.index(stlpec)
riadok = 8 - (int(n[1]))
for x in range(8):
    zznm[x] = []
    for i in range(8):
        if riadok == x:
            zznm[x].append(1)
        elif stlpec == i:
            zznm[x].append(1)
        elif abs(x - riadok) == abs(i - stlpec):
            zznm[x].append(1)
        else:
            zznm[x].append(0)

