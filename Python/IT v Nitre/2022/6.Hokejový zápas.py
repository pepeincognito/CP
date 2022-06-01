#h-10:17,d-19:1,h-35:10,h-38:15,h-59:40,d-59:59
lst = [str(x) for x in input().split(",")]
dom = 0
hos = 0
for x in lst:
	if x[0] =="d":
		dom+=1
	else:
		hos+=1
time = 0
if dom>hos:
	d = 0
	ct = 0
	for x in lst:
		ct+=1
		if x[0] == "d":
			d += 1
		if d == hos+1:
			time = lst[ct-1][2:7]
			break
else:
	d = 0
	ct = 0
	for x in lst:
		ct+=1
		if x[0] == "h":
			d += 1
			
		if d == dom+1:
			time = lst[ct-1][2:7]
			break
			
print(f"{dom}:{hos}")
time = int(time[0:2])+int(time[3:5])/100


if time <20:
	print(1)
elif time <40:
	print(2)
else:
	print(3)
