alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
n = int(input())
lst = []
for x in range(n):
    lst.append([str(i) for i in input()])
lst = lst[::-1]
for x in lst:
    for j in range(len(x)):
        if x[j] != "-":
            x[j] = alp[0]
            alp.pop(0)
for x in lst[::-1]:
    print("".join(x))