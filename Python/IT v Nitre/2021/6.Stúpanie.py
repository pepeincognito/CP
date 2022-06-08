lst = [int(x) for x in input().split(", ")]
stp = 0
for x in range(len(lst)-1):
  if lst[x+1] - lst[x]>0:
    stp += lst[x+1] - lst[x]
print(stp)