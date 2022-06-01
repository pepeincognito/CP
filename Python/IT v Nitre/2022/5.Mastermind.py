pin = [str(x) for x in input()]
guess = [str(x) for x in input()]
p = 0
f = 0
for x in range(4):
	if guess[x] == pin[x]:
		guess[x] = "x"
		pin[x] = "x"
		p+=1
for x in range(4):
	if guess[x] in pin and guess[x]!="x":
		f +=1
if p+f ==0:
	print('nic')
else:
	print(f"{p*'P'}{f*'F'}")
		