slk = {}
lst = []
while True:
    b = input()
    if b =="KONIEC":
        break
    lst = []
    while True:

        a = input()
        if a == "---":
            break
        lst.append(a)

    slk[b] = []
    for x in lst:
        slk[b].append(x)


for x in slk:
    print(x)

    for i in slk[x]:
        print(i)
    print("---")
print("KONIEC")