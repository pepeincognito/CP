lst = [int(x) for x in input().split(",")]
n = 0
psikovia = []
for x in range(1, 6):
    if lst.count(x) > n:
        psikovia = [x]
        n = lst.count(x)
    elif lst.count(x) == n:
        psikovia.append(x)

per = n / len(lst) * 100
for x in psikovia:
    print(f"{x} {round(per, 1)}")
