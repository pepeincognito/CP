fix = [28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 29]
fixp = [28, 28, 28, 28, 29, 28, 28, 28, 28, 28, 28, 28, 29]
klasp = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 31, 31]
klas = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 31, 31]
n = [str(x) for x in input().split(".")]
day = int(n[0])
month = int(n[1])
prestup = n[2]
ct = 0

if prestup == "p":
	ct = sum(klasp[0:month ]) + day
else:
	ct = sum(klas[0:month ]) + day
month = 0
day = 0
x = 0
if prestup == "p":
	while True:
		if ct>=fixp[x]:
			month+=1
			ct -=fix[x]
		else:
			day = ct
			break

else:
	while True:
		if ct>=fix[x]:
			month+=1
			ct -=fix[x]
		else:
			day = ct
			break
print(f"{day}.{month}.{prestup}")