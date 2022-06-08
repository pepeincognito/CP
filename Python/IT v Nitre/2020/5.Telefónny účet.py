import math
n = sum([int(x) for x in input().split()])
hod = math.floor(n/3600)
min = math.floor((n-hod*3600)/60)
sec = math.floor((n-min*60-hod*3600))
print(f"{hod} hod {min} min {sec} sek")