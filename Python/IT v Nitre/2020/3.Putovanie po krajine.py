lst = input().split("#")
x, y = 0, 0
for i in lst:
	if i == "S":
		y += 1
	elif i == "SV":
		x += 1
		y += 1
	elif i == "V":
		x += 1
	elif i == "JV":
		x += 1
		y -= 1
	elif i == "J":
		y -= 1
	elif i == "JZ":
		x -= 1
		y -= 1
	elif i == "Z":
		x -= 1
	elif i == "SZ":
		y += 1
		x -= 1
print(f"{x},{y}")
