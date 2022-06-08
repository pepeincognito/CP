"""3 4
1 1 1 1
0 0 0 1
1 0 0 0
3"""
n, m = [int(x) for x in input().split()]

slk = {}
lst = []
for i in range(n):
    slk[i] = [int(x) for x in input().split()]
x = int(input())
for i in slk:

    for j in range(len(slk[i]) - x + 1):
        # print(slk[i][j:j + x])
        if slk[i][j:j + x].count(0) == x and i + 1 not in lst:
            lst.append(i + 1)
if len(lst) != 0:
    print(f"ano {' '.join([str(x) for x in lst])}")
else:
    print("nie")
