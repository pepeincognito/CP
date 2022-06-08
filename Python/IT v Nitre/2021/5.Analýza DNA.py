dna = input()
n = int(input())
a = 0
for x in range(len(dna) - n + 1):
    vzorka = dna[x:x + n]
    if vzorka == vzorka[::-1]:
        a += 1

print(a)