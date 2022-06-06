# 2 2 DDDLDDDD
import math

d, l, lst = [str(x) for x in input().split()]
x = int(d)
y = int(l)
cx = x
cy = y
lst = [str(x) for x in lst]
ct = 0
smery = ["h", "p", "d", "l"]
for i in lst:
	if i == "P":
		ct += 1
	elif i == "L":
		ct-=1
	elif i == "D":
		smer = smery[ct%4]
		if smer == "h":
			y+=1
		elif smer == "p":
			x+=1
		elif smer == "d":
			y-=1
		elif smer == "l":
			x-=1
print(f"Pozicia: {x} {y}")
print(f"Vzdialenost: {round(math.sqrt((x - cx) ** 2 + (y - cy) ** 2),2)}")
"""Pozicia: 2 4
Vzdialenost: 4.47"""
