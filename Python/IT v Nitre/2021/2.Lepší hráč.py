prvy = [int(x) for x in input().split(",")]
druhy = [int(x) for x in input().split(",")]
if len(prvy)>len(druhy):
	print("prvy")
else:
	if len(druhy) > len(prvy):
		print("druhy")
	else:
		if sum(prvy)>sum(druhy):
			print(f"druhy o {sum(prvy)-sum(druhy)} s")
		elif sum(druhy)>sum(prvy):
			print(f"prvy o {sum(druhy)-sum(prvy)} s")
		else:
			print("remiza")